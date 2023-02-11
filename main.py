# IMPORTS
import os

from imtovid.get_files import *
from compile import *

SRC_DIR = input("src directory > ")
AUDIO_LINK = input("yt audio link > ")
EXTENSION = input("image extension > ")
SECONDS_PER_IMAGE = float(input("seconds per image > "))
FPS = 30


def main():
    # Move all mp4 files to the temp directory
    files_in_dir = os.listdir()

    for file in files_in_dir:
        if file.split(".")[len(file.split(".")) - 1] == "mp4":
            print(f"Moving {file} to temp directory...\n")
            os.system(f"mv {file} ./temp")

    files_arr = get_files(SRC_DIR, EXTENSION)
    compile(SRC_DIR, files_arr, SECONDS_PER_IMAGE, FPS, AUDIO_LINK)

    # Clear Temp
    os.system("rm -rf ./temp/image/* ./temp/audio/* output.mp4 fixed.mp4")


if __name__ == "__main__":
    main()
