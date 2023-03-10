from moviepy.editor import (
    AudioFileClip,
    ImageClip,
    CompositeAudioClip,
    vfx,
    afx,
    concatenate_videoclips,
)

import time
from imtovid.process_image import *
from imtovid.download_from_yt import *
import os


def compile(location, files, seconds_per_image, fps, audio_link):
    clips = []

    start_time = time.time()

    print("\n==========================================")
    print("============ Processing Files ============")
    print("==========================================\n")

    for i, file in enumerate(files):
        clips.append(
            ImageClip(
                resize_clip_and_overlay_on_blurred_image(
                    f"{location}/{file}", file)
            )
            .set_duration(seconds_per_image)
            .set_start(seconds_per_image * (i + 1) + 0.2)
            .crossfadein(0.2)
            .crossfadeout(0.2)
        )

    print("\n===========================================")
    print("============ Downloading Audio ============")
    print("===========================================\n")

    get_audio_from_youtube(audio_link)
    audio = (
        AudioFileClip("./temp/audio/audio.mp3")
        .subclip(0, (len(files) - 1) * seconds_per_image)
        .fx(afx.audio_fadein, 1)
        .fx(afx.audio_fadeout, 1)
    )

    print("\n=========================================")
    print("============ Rendering Video ============")
    print("=========================================\n")

    video_clip = concatenate_videoclips(clips, method="compose")
    video_clip.audio = CompositeAudioClip([audio])
    video_clip.write_videofile(
        "output.mp4", fps=fps, remove_temp=True, codec="libx264", audio_codec="mp3"
    )

    # Fix the video rendered by movie.py
    os.system("ffmpeg -i output.mp4 -c:v libx264 -c:a aac fixed.mp4")

    # Add thumbnail to video
    os.system(
        f"ffmpeg -i fixed.mp4 -i ./temp/image/{files[0]} -map 1 -map 0 -c copy -disposition:0 attached_pic final.mp4"
    )

    end_time = time.time()

    print(f"\nTotal Time Elapsed: {end_time - start_time}")
