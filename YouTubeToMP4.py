from pytube import YouTube
import os
from pytube.cli import on_progress
import re
import colorama
from colorama import Back, Fore, Style



def download_complete(stream, file_path):
    print("\n")
    print(Fore.GREEN + "Downloaded to: " + file_path)
    print("\n")


def get_dir():

    current_dir = os.getcwd()

    print("\n1: Download to Project Directory: " + current_dir)
    print("2: Custom Directory: ")

    option = str(input())
    dir = ""

    if option == "2":
        print("Enter Dir: ", end="")
        dir = str(input())

    else:
        dir = current_dir

    while os.path.exists(dir) == False:
        print("Directory Invalid. Please try again.")
        print("Enter Dir: ", end="")
        dir = str(input())

    return dir


def get_audio(tube):

    audio = tube.streams.get_audio_only()

    parent_dir = str(get_dir())

    path = os.path.join(parent_dir, "AUDIO")

    if os.path.exists(path) == False:
        os.mkdir(path)

    fileName = re.sub("\W+", "", tube.title)

    audio.download(output_path=path, filename=fileName + ".mp3", skip_existing=True)


def get_vid(tube):

    video = tube.streams.get_highest_resolution()

    parent_dir = str(get_dir())

    path = os.path.join(parent_dir, "VIDEO")

    if os.path.exists(path) == False:
        os.mkdir(path)

    fileName = re.sub("\W+", "", tube.title)

    video.download(output_path=path, filename=fileName + ".mp4", skip_existing=True)


# ----------START------------
colorama.init(autoreset = True)


print(Fore.BLUE + "YOUTUBE TO MP4")



print(
    "WARNING: You will be promted to sign into your YouTube acccount on 1st launch using OAuth"
)



try:
    print("video URL: ", end="")

    link = str(input())

    tube = YouTube(
        link, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress
    )

    tube.register_on_complete_callback(download_complete)

    print("Title: ", tube.title)

    print("1. Video .MP4\n2. Audio .MP3")

    out_choice = str(input())

    if out_choice == "1":
        get_vid(tube)

    elif out_choice == "2":
        get_audio(tube)


except:
    print("ERROR")
    print("APP CLOSING...")
