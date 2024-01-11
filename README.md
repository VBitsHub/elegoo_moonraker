# elegoo_moonraker
Modified elegoo neptune 4 max's moonraker to support thumbnails for Prusa slicer, add support for Orca slicer
Backup your original ~/moonraker/moonraker/components/file_manager/metadata.py before copying this version over. After copying the file over using winscp or any other sftp software, reboot the machine.

You should now see the correct information and thumbnails in fluidd and the elegoo touchscreen. This does not update existing files, only files processed after the update.

Update 1/11/2024: Made a request to SoftFever to change the background to the color used in the neptuneTSfix instead of bright white. Also made the changes myself in the current v2.0.0-dev build. If you can't wait for an official update. You can download the one dll that I compiled today in the releases section. To use, backup your existing OrcaSlicer.dll in your Orcaslicer folder than  replace with the one in the releases section.

Update 1/9/2024: Added an updater than can be run on the printer to update the metadata.py with the current one on github if needed. Just place in your /home/mks/ folder. You may need to run "chmod 777 update_metadata.py" afterwards if you cannot execute it.

Update 1/8/2024: Finally had time to install v1.9.0, didn't work for me out of box like it did the few that messaged me, but was able to locate the issue.
                 Updated metadata.py to support searching for gimage and simage in footer_data to fix touchscreen not showing. You must select ColPic for "Format of G-Code thumbnails" and define the G-Code Thumbnail sizes as: 200x200, 160x160. You need to add BOTH separated with a comma.
                 
Update 1/6/2024: NeptuneTSFix is no longer needed if using version 1.9.0+ of OrcaSlicer. Select ColPic for "Format of G-Code thumbnails"

If you wish to see the thumbnail on the touchscreen, download the neptuneTSfix.exe under releases and add it to post processing for Prusa ~~and/or Orca~~.
NeptuneTSFix is based off of Molodos Neptune Cura
