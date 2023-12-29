# elegoo_moonraker
Modified elegoo neptune 4 max's moonraker to support thumbnails for Prusa slicer, add support for Orca slicer
Backup your original ~/moonraker/moonraker/components/file_manager/metadata.py before copying this version over. After copying the file over using winscp or any other sftp software, reboot the machine.

You should now see the correct information and thumbnails in fluidd and the elegoo touchscreen. This does not update existing files, only files processed after the update.

If you wish to see the thumbnail on the touchscreen, download the neptuneTSfix.exe under releases and add it to post processing for Prusa and/or Orca
NeptuneTSFix is based off of Molodos Neptune Cura
