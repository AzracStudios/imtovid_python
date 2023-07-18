# IMPORTS
import os
import yaml
from get_files import *
from compile import *

SRC_DIR = ""
AUDIO_LINK = ""
EXTENSION = ""
SECONDS_PER_IMAGE = 0
FPS = 30
WIDTH = 0
HEIGHT = 0


def main():
    # Load config
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        SRC_DIR = config["image"]["src"]
        SECONDS_PER_IMAGE = config["image"]["seconds_per_image"]
        EXTENSION = config["image"]["extension"]
        FPS = config["video"]["frame_rate"]
        AUDIO_LINK = config["audio"]["yt_url"]
        WIDTH = config["video"]["width"]
        HEIGHT = config["video"]["height"]

    # Move all mp4 files to the temp directory
    # files_in_dir = os.listdir()

    # for file in files_in_dir:
    #     if file.split(".")[len(file.split(".")) - 1] == "mp4":
    #         print(f"Moving {file} to temp directory...\n")
    #         os.system(f"mv {file} ./temp")

    files_arr = get_files(SRC_DIR, EXTENSION)
    if not files_arr: return

    compile(SRC_DIR, files_arr, SECONDS_PER_IMAGE, FPS, AUDIO_LINK, WIDTH, HEIGHT)

    # Clear Temp
    os.system("rm -rf ./temp/image/* ./temp/audio/* output.mp4 fixed.mp4")


if __name__ == "__main__":
    main()
