# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:59:41 2021

@author: david thonnard
@email: thonnard.david@gmail.com

python script to select a specific time frame from a video
"""

import os

# where am I?
print("Working directory: " + os.getcwd())

# select video file
input = '351-02177 - 4-02201.mp4'

# create output file
output = 'output test.mp4'

# select time frame (format: hh:mm:ss.xxx)
start = '00:03:50.0'
end = '00:05:55.0'

# command (don't change this)
command = 'ffmpeg -ss ' + start + ' -i ' + '"' + input + '"' + ' -c copy -t ' + end + ' ' + '"' + output + '"'

# run command
os.system(command)



# references
# https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video
# https://stackoverflow.com/questions/55564929/how-to-write-this-ffmpeg-command-in-python