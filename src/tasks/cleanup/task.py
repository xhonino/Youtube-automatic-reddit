import os
import glob

paths = [
    # r"C:\Users\Olsi\PycharmProjects\kot\data\thumbnails\*.png",
    # r"C:\Users\Olsi\PycharmProjects\kot\data\video\*.mp4",
    r"C:\Users\Olsi\PycharmProjects\kot\data\audio\*.mp3",
]

def cleanup(context):
    for path in paths:
        files = glob.glob(path)
        for f in files:
            os.remove(f)
