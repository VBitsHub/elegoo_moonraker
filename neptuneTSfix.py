import argparse
import base64
import platform
from argparse import Namespace
from array import array
from ctypes import CDLL
from os import path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage

class neptuneTSfix:
    def __init__(self):
        args: Namespace = self._parse_args()
        self._gcode: str = args.gcode
        self._thumbnail: QImage = self._get_q_image_thumbnail()

    @classmethod
    
    def _parse_args(cls) -> Namespace:
        parser = argparse.ArgumentParser(
            prog="neptuneTSfix v0.1",
            description="Post script to add thumbnail to Elegoo Touch Screen")
        parser.add_argument("gcode", help="Thumbnail gcode based on Cura snapshot pixel data", type=str)
        return parser.parse_args()

    def _get_base64_thumbnail(self) -> str:
        found: bool = False
        base64_thumbnail: str = ""
        with open(self._gcode, "r", encoding="utf8") as file:
            for line in file.read().splitlines():
                if not found and (line.startswith("; thumbnail begin 300x300") or line.startswith("; thumbnail begin 600x600") or line.startswith("; thumbnail begin 200x200") or line.startswith("; thumbnail begin 48x48")):
                    found = True
                elif found and line == "; thumbnail end":
                    return base64_thumbnail
                elif found:
                    base64_thumbnail += line[2:]

        raise Exception("No thumbnail found")
                        
    def _get_q_image_thumbnail(self) -> QImage:
        base64_thumbnail: str = self._get_base64_thumbnail()
        thumbnail = QImage()
        thumbnail.loadFromData(base64.decodebytes(bytes(base64_thumbnail, "UTF-8")), "PNG")

        return thumbnail

    def _generate_gcode_prefix(self) -> str:
        gcode_prefix: str = ""
        gcode_prefix += self._parse_thumbnail(self._thumbnail, 200, 200, "gimage")
        gcode_prefix += self._parse_thumbnail(self._thumbnail, 160, 160, "simage")        

        return gcode_prefix

    def add_thumbnail_prefix(self) -> None:
        g_code: str
        with open(self._gcode, "r", encoding="utf8") as file:
            g_code: str = file.read()

        if ';gimage:' not in g_code and ';simage:' not in g_code:
            gcode_prefix: str = self._generate_gcode_prefix()
            with open(self._gcode, "w", encoding="utf8") as file:
                file.write(gcode_prefix + g_code)

    @classmethod
    def _parse_thumbnail(cls, img: QImage, width: int, height: int, img_type: str) -> str:
        img_type = f";{img_type}:"
        sys: str = platform.system().lower()
        p_dll = CDLL("ColPic_X64.dll"))

        result = ""
        b_image = img.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
        img_size = b_image.size()
        color16 = array('H')
        try:
            for i in range(img_size.height()):
                for j in range(img_size.width()):
                    pixel_color = b_image.pixelColor(j, i)
                    r = pixel_color.red() >> 3
                    g = pixel_color.green() >> 2
                    b = pixel_color.blue() >> 3
                    rgb = (r << 11) | (g << 5) | b
                    color16.append(rgb)

            from_color16 = color16.tobytes()
            output_data = array('B', [0] * img_size.height() * img_size.width()).tobytes()
            result_int = p_dll.ColPic_EncodeStr(from_color16, img_size.height(), img_size.width(), output_data,
                                                img_size.height() * img_size.width(), 1024)

            data0 = str(output_data).replace('\\x00', '')
            data1 = data0[2:len(data0) - 2]
            each_max = 1024 - 8 - 1
            max_line = int(len(data1) / each_max)
            append_len = each_max - 3 - int(len(data1) % each_max)

            for i in range(len(data1)):
                if i == max_line * each_max:
                    result += '\r;' + img_type + data1[i]
                elif i == 0:
                    result += img_type + data1[i]
                elif i % each_max == 0:
                    result += '\r' + img_type + data1[i]
                else:
                    result += data1[i]
            result += '\r;'
            for j in range(append_len):
                result += '0'

        except Exception as e:
            raise e

        return result + '\r'


if __name__ == "__main__":
    thumbnail_generator: neptuneTSfix = neptuneTSfix()
    thumbnail_generator.add_thumbnail_prefix()
        
