import numpy as np
import os, sys


# Create the file location for where the extracted videos into frames go
def create_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError:
        print("Folder already exists")


# Converts the videos into frames and places them inside the associated created folder
def convert_videos(file_location, folder_name):
    count = 1
    for x in os.listdir("./" + file_location + '/'):
        create_folder("./sample_images/" + folder_name + "/video_" + str(count) + "_frames")
        os.system("ffmpeg -i sample_images/" + folder_name + "/" + x + " -r 4 sample_images/"
                  + folder_name + "/video_" + str(count) + "_frames/image%05d.jpg -hide_banner")
        count += 1


# Saves the audio from each video into a specified directory
def convert_audio(file_location, folder_name):
    count = 0
    create_folder("./blue_background_sample_images/audio_clips")
    for x in os.listdir("./" + file_location + "/"):
        # os.system("ffmpeg -i sample_images/" + folderName + "/" + x + " -f mp3 -vn sample_images/" + folderName
        # + "/audio_clips/audio_clip_" + str(count) + ".mp3 -hide_banner")
        os.system("ffmpeg -i blue_background_sample_images/" + x
                  + " -f mp3 -vn blue_background_sample_images/audio_clips/audio_clip_" + str(count) + ".mp3 -hide_banner")
        count += 1
