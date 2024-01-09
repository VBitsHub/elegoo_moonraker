# !/bin/bash

# Updater for VBitsHub Elegoo Moonraker.

echo "Updater for VBitsHub Elegoo Moonraker"

# GitHub repository information
file_path="elegoo_moonraker/master/metadata.py"
local_file="/home/mks/moonraker/moonraker/components/file_manager/metadata.py"
raw_base_url="https://raw.githubusercontent.com/VBitsHub"

# Date for creating a backup
backup_date=$(date +"%Y%m%d")

# Download the file from GitHub
wget "${raw_base_url}/${file_path}" -P "/home/mks/temp/"

# Compare the downloaded file with the local file
if diff /home/mks/temp/metadata.py "${local_file}" >/dev/null; then
	echo "File is up to date...."
else
	echo "Updating file.."
	# Create a backup by appending today's date to the existing file name
	backup_file="${local_file}.${backup_date}"
	mv "${local_file}" "${backup_file}"

	# Replace the local file with the downloaded file
	mv /home/mks/temp/metadata.py "${local_file}"
	chmod 777 "${local_file}"
	echo "File has been updated, downloaded, and a backup has been created: ${backup_file}"
fi

echo "Cleaning up..."
rm /home/mks/temp/metadata.py
