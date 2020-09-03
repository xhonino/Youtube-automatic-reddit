import os
import glob

def cleanup(context):

    os.chdir('../')
    cwd = os.getcwd()
    os.chdir('src')

    thumbnail_path = fr'{cwd}\data\thumbnails\{context["video_id"]}.png'
    video_path = fr'{cwd}\data\video\{context["video_id"]}.mp4'
    post = context["post"]
    subreddit = 'AskReddit'
    description = post.title + f" (/r/{subreddit})"

    os.mkdir(rf'{cwd}\VIDEOS\{context["video_id"]}')
    os.rename(thumbnail_path, rf'{cwd}\VIDEOS\{context["video_id"]}\thumbnail.png')
    os.rename(video_path, rf'{cwd}\VIDEOS\{context["video_id"]}\video.mp4')
    with open(rf'{cwd}\VIDEOS\{context["video_id"]}\Video Info.txt','a') as file:
        file.writelines(f'TITLE: {post.title}\n')
        file.writelines(f'DESC: {description}\n')
        file.writelines(f'URL: {context["url"]}\n')

    paths = [
        rf'{cwd}\data\thumbnails\*.png',
        rf'{cwd}\data\video\*.mp4',
        rf'{cwd}\data\audio\*.mp3',
    ]

    for path in paths:
        files = glob.glob(path)
        for f in files:
            os.remove(f)

