# elegoo_moonraker
Modified elegoo neptune 4 plus/max's (works with N4 and N4Pro) moonraker to support thumbnails for Prusa slicer, add support for Orca slicer, Slic3r, Slic3rPE, SuperSlicer
*No longer requires post-processing for PrusaSlicer, OrcaSlicer, and SuperSlicer

Backup your original ~/moonraker/moonraker/components/file_manager/metadata.py before copying this version over. **Copy both metadata.py and lib_col_pic.py** to the ~/moonraker/moonraker/components/file_manager/metadata.py folder.  After copying the file over using winscp or any other sftp software, reboot the machine.

You should now see the correct information and thumbnails in fluidd and the elegoo touchscreen. This does not update existing files, only files processed after the update.

![orca_1](https://github.com/VBitsHub/elegoo_moonraker/assets/62845219/207207ef-c9b5-4514-9a51-ad72684ecd93)
![20240124_140841](https://github.com/VBitsHub/elegoo_moonraker/assets/62845219/c4264911-af27-4be2-8b8a-9e9892b9fece)



-----------------
Update 1/19/2024: 
- Updated code to use Pillow instead of PyQT6 so people do not have to build/install PyQT6
- Bug fix for thumbnail miniature 32x32 creation.
- Merged slic3r and slic3rPE
- Added Support for SuperSlicer
- Required Files to copy to machine are: metadata.py and lib_col_pic.py
- Select PNG for output and put any resolution for the image. For example: 300x300 or 500x500, Metadata.py will do the rest.
- For OrcaSlicer you can select either PNG or colpic (colpic requires both 200x200, 160x160)
- Updated update_metadata.sh to reflect adding lib_col_pic.py

-----------------
Update 1/18/2024: 
- Updated to process PNG images for touchscreen on elegoo neptune 4. Prusa and Orca thumbnails no longer need to run any post-processing scripts, select PNG for output and use any resolution. For example 300x300 or 500x500.
- Requires building/installing PyQT6 for armbian.

-----------------
Update 1/15/2024: 
- PR and merge has been completed https://github.com/SoftFever/OrcaSlicer/pull/3647, should be available in future updates to OrcaSlicer. 

-----------------
Update 1/11/2024: 
- Made a request to SoftFever to change the background to the color used in the neptuneTSfix instead of bright white (https://github.com/SoftFever/OrcaSlicer/pull/3647). 
- Also made the changes myself in the current v2.0.0-dev build. If you can't wait for an official update. You can download the one dll that I compiled today in the releases section.
- To use, backup your existing OrcaSlicer.dll in your Orcaslicer folder than  replace with the one in the releases section.

-----------------
Update 1/9/2024: 
- Added an updater than can be run on the printer to update the metadata.py with the current one on github if needed. Just place in your /home/mks/ folder. You may need to run "chmod 777 update_metadata.py" afterwards if you cannot execute it.

-----------------
Update 1/8/2024: 
- Finally had time to install v1.9.0, didn't work for me out of box like it did the few that messaged me, but was able to locate the issue.
- Updated metadata.py to support searching for gimage and simage in footer_data to fix touchscreen not showing. You must select ColPic for "Format of G-Code thumbnails" and define the G-Code Thumbnail sizes as: 200x200, 160x160. You need to add BOTH separated with a comma.
                 
-----------------
Update 1/6/2024: 
- NeptuneTSFix is no longer needed if using version 1.9.0+ of OrcaSlicer. Select ColPic for "Format of G-Code thumbnails"

~~If you wish to see the thumbnail on the touchscreen, download the neptuneTSfix.exe under releases and add it to post processing for Prusa and/or Orca~~.
NeptuneTSFix is based off of Molodos Neptune Cura
lib_col_pic.py was used from https://github.com/Molodos/ElegooNeptuneThumbnails-Prusa
