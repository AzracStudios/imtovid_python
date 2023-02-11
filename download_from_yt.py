from pytube import YouTube
from moviepy.editor import VideoFileClip
import time
import os


def get_audio_from_youtube(link):
    try:
        vid = YouTube(link)
        startTime = time.time()

        print(
            f"Video Title: {vid.title}\nVideo Author: {vid.author}\nVideo Views: {vid.views}\nVideo Upload Date: {vid.publish_date}\n\nDownloading as MP4..."
        )
        vid.streams.first().download("./temp/audio", filename=f"audio.mp4")

        print("Download Completed!")
        print("Extracting Audio")

        inp = VideoFileClip(f"./temp/audio/audio.mp4")
        out = inp.audio

        print("Saving Audio\n")

        out.write_audiofile(f"./temp/audio/audio.mp3")

        print("\nRemoving MP4...")
        os.remove(f"./temp/audio/audio.mp4")

        print("Completed!")

    except Exception as e:
        print(f"Couldn't Download Video: {e}")
