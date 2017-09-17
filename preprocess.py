from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import subprocess
import os
import sys

# Pre...
output_dir_base = 'D:\Path\To\Files'
textfile_path = 'negative_filenames.txt' # file paths

# Read the text file
with open(textfile_path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
files_list = [x.strip() for x in content]
# remove all spaces
# files_list = [x.replace(" ", "") for x in content]

 
# It already save the video file using the named defined by output_name.
for file_num, file_path_input in enumerate(files_list, start=1):
    # Get the file name without extension
    file_name = os.path.basename(file_path_input)
    raw_file_name = os.path.basename(file_name).split('.')[0]
    raw_file_name = raw_file_name.replace(" ", "")
    print('raw_file_name=%s' % (raw_file_name))
    file_dir_input = os.path.dirname(file_path_input)
    print('file_dir_input=%s' % (file_dir_input))
    file_dir_output = output_dir_base
    print('file_dir_output=%s' % (file_dir_output))
    if not os.path.exists(file_dir_output):
        os.makedirs(file_dir_output)
    file_path_output = file_dir_output + '\\' + raw_file_name + '.mp4'
    print('processing file: %s' % file_path_input)

    subprocess.call(
        ['ffmpeg', '-y', '-i',  file_path_input,  '-vf', 'scale=299:299,setsar=1:1',
        '-r', '30', '-vcodec', 'nvenc', '-b:v', '3M', file_path_output])
print('file %s saved' % file_path_output)
