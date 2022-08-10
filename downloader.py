from pytube import YouTube
from pathlib import Path
from moviepy.editor import *
import os

def download_video(link):
    yt = YouTube(link)

    stream = yt.streams.get_highest_resolution()

    try:
        stream.download()
        return (yt.title, yt.views, yt.length, yt.description, yt.rating, "Download completed")
    except Exception as e:
        return ("","","","","","Download failed")

def download_mp3(link):
    print("in download mp3")
    yt = YouTube(link)

    stream = yt.streams.get_highest_resolution()
    # print("before try")
    try:
        stream.download()
        mp4_file = (str(Path(__file__).resolve().parent) + "\\" + str(yt.title) + ".mp4")
        # print(mp4_file)
        mp3_file = (str(Path(__file__).resolve().parent) + "\\" + str(yt.title) + ".mp3")
        # print(mp3_file)
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        os.remove(mp4_file) # add exception handling
    except Exception as e:
        print(e)
