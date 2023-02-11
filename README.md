# ImToVid

## Introduction
ImToVid is an application that takes images on the disk, compiles them into a video, and adds a youtube video as a backing track to it. This application uses opencv, moviepy and pytube

## OpenCv
OpenCv is used in this application to prep the images. It creates a blurred version of the image, and stretches it to match the video resolution. It then layers the original image on top of it, and writes it to the disk

## Pytube
Pytube downloads the audio off of youtube, given an audio link. It first downloads the video at the given link. It then uses moviepy to extract the audio and write it to the disk

## MoviePy
Moviepy is used in this application to put all the images into a sequence with transitions, and adds the audio file as a backing track, renders the video and writes it to the disk. Then, ffmpeg is used to set the thumbnail and fix version discrepancies


## Run the application
- Clone or download the github repository
- Install requirements
- Run

`$ git clone git@github.com:AzracStudios/imtovid_python`

`$ cd imtovid_python`

`$ pip install -r requirements.txt`

`$ python3 main.py`

Before running the application, make sure to put all the images into a directory, and name them in the order you want them to appear, starting from 0. Then, copy the path of this directory. Also copy the youtube video link that you want as the backing track.

## Resources
OpenCv documentation: https://opencv24-python-tutorials.readthedocs.io/en/latest/

Overlay images: https://pyimagesearch.com/2016/03/07/transparent-overlays-with-opencv/

MoviePy documentation: https://zulko.github.io/moviepy/

PyTube documentation: https://pytube.io/en/latest/

FFMPEG documentation: https://ffmpeg.org/ffmpeg.html
