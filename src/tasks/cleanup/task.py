import os
import glob

def cleanup(context):
    thumbnail_path = fr'C:\Users\Olsi\PycharmProjects\kot\data\thumbnails\{context["video_id"]}.png'
    video_path = fr'C:\Users\Olsi\PycharmProjects\kot\data\thumbnails\{context["video_id"]}.mp4'
    post = context["post"]
    subreddit = 'AskReddit'
    description = post.title + f" (/r/{subreddit})"

    os.mkdir(rf'C:\Users\Olsi\PycharmProjects\kot\VIDEOS\{context["video_id"]}')
    os.rename(thumbnail_path, r"C:\Users\Olsi\PycharmProjects\kot\VIDEOS\thumbnail.png")
    os.rename(video_path, r"C:\Users\Olsi\PycharmProjects\kot\VIDEOS\video.mp4")
    with open(rf'C:\Users\Olsi\PycharmProjects\kot\VIDEOS\{context["video_id"]}\Video Info.txt','a') as file:
        file.writelines(f'TITLE: {post.title}\n')
        file.writelines(f'DESC: {description}\n')
        file.writelines(f'URL: {post.url}\n')

    paths = [
        r"C:\Users\Olsi\PycharmProjects\kot\data\thumbnails\*.png",
        r"C:\Users\Olsi\PycharmProjects\kot\data\video\*.mp4",
        r"C:\Users\Olsi\PycharmProjects\kot\data\audio\*.mp3",
    ]

    for path in paths:
        files = glob.glob(path)
        for f in files:
            os.remove(f)

