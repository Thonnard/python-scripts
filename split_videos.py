#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:42:41 2021

@author: david thonnard
@email: thonnard.david@gmail.com

python script to split video files in chunks without affect quality
"""

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

# where am I?
print("Working directory: " + os.getcwd())

# select video file
required_video_file = "s07-cam2.avi"
print("Selected video file: " + required_video_file)

# set start (seconds)
start = 0

# get duration of full video (seconds)
length = int(VideoFileClip(required_video_file).duration)

# set chunk duration (seconds)
chunk = 600

# number of files to create
number_of_chunks = int(round(length/chunk,0))

# create list for chunks
time_range = range(start,length,chunk)

# create video chunks
print("Duration source video: " + str(length) + "s")
print("Number of chunks: " + str(number_of_chunks))
print("Chunk duration: " + str(chunk) + "s")
print("Start from: " + str(start))
for index, i in enumerate(time_range, start=1):
    if(i<max(time_range) and index <= number_of_chunks):
        starttime = i
        endtime = i + chunk
        print("\nRun:" + str(index))
        print("Starttime: " + str(starttime))
        print("Endtime: " + str(endtime))
        filename=required_video_file[:- 4] + "_" + str(index) + "_(" + str(starttime) + "-" + str(endtime) + ")" + required_video_file[-4:]
        ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=filename)
        print("Output: " + filename)
