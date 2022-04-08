# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:53:39 2022

@author: david thonnard
@email: thonnard.david@gmail.com

python script to crop videos
"""

# libraries
import os

# function
def cropVideo(input, width, height, x, y, output='cropped.mp4'):
    crop = '"crop='+str(width)+':'+str(height)+':'+str(x)+':'+str(y)+'"'
    command = 'ffmpeg -y -i ' + '"' + input + '"' + ' -vf ' + crop + ' -c:v libx265 -crf 17 -c:a copy ' + '"' + output + '"'
    os.system(command)
  
# crop
cropVideo('test_camera_nathalia_28_03_2022.avi', 880, 880, 520,220,output='test.mp4')




# references
# https://video.stackexchange.com/questions/4563/how-can-i-crop-a-video-with-ffmpeg
# https://stackoverflow.com/questions/33378548/ffmpeg-crop-a-video-without-losing-the-quality
# https://stackoverflow.com/questions/39788972/ffmpeg-overwrite-output-file-if-exists