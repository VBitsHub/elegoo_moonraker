# !/bin/bash

# Updater for VBitsHub Elegoo Moonraker.

echo "Updater for VBitsHub Elegoo Moonraker"

# GitHub repository information
file_path="elegoo_moonraker/master/metadata.py"
file_path_libcolpic="elegoo_moonraker/master/lib_col_pic.py"
local_file="/home/mks/moonraker/moonraker/components/file_manager/metadata.py"
local_file_libcolpic="/home/mks/moonraker/moonraker/components/file_manager/lib_col_pic.py"

raw_base_url="https://raw.githubusercontent.com/VBitsHub"

# Date for creating a backup
backup_date=$(date +"%Y%m%d")

# Download the file from GitHub
wget "${raw_base_url}/${file_path}" -P "/home/mks/temp/"
wget "${raw_base_url}/${file_path_libcolpic}" -P "/home/mks/temp/"

if diff /home/mks/temp/lib_col_pic.py "${local_file_libcolpic}" >/dev/null; then
	echo "lib_col_pic.py is up to date..."
else
	echo "Updating lib_col_pic.py..."
	backup_file="${local_file_libcolpic}.${bacup_date}"
	mv "${local_file_libcolpic}" "${backup_file}"
	
	mv /home/mks/temp/lib_col_pic.py "${local_file_libcolpic}"
	echo "Lib_col_pic.py has been updated..."

# Compare the downloaded file with the local file
if diff /home/mks/temp/metadata.py "${local_file}" >/dev/null; then
	echo "Metadata.py is up to date...."
else
	echo "Updating metadata.py.."
	# Create a backup by appending today's date to the existing file name
	backup_file="${local_file}.${backup_date}"
	mv "${local_file}" "${backup_file}"

	# Replace the local file with the downloaded file
	mv /home/mks/temp/metadata.py "${local_file}"
	chmod 777 "${local_file}"
	echo "Metadata.py has been updated, downloaded, and a backup has been created: ${backup_file}"
fi

echo "Cleaning up..."
rm /home/mks/temp/metadata.py
rm /home/mks/temp/lib_col_pic.py
