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
    description = f"\n{post.title} [r/AskReddit] Reddit Stories\n\nWe at StoryMonkey research the top posts of Reddit subreddits like AskReddit and r/ama  and  try to repurpose the stories to best suit the viewer. The Reddit Stories may be funny, cringe or even creppy but this time there some choosen top comments from askreddit who share some of the most unbelievable stories they witnessed.\n\nDisclaimer: All content of this video is used for dramatization and creative use only and are not representative of the individuals, events, and happenings that are told in the stories. The stories are transformative representations shared by anonymous individuals on different subreddit of Reddit. \n\nDon't forget to Subscribe and to Ring The Bell\n\nSubscribe for everyday Videos\nhttps://www.youtube.com/channel/UCbPl1jArnXnYf-xY__qA0hg\n\nShare some stories with your fellas on the comment below\n\nFeel free to contact me for any inquiry storymonkey2020@gmail.com"
    tags = "r/askreddit,askreddit,updoot everything,unpopular opinions reddit,reddit,reddit stories,ask reddit,reddit story,updoot,reddit funny stories,reddit tales,updoot reddit,askreddit funny,reddit jar,planet reddit,storytime with reddit,funny reddit stories,reddit and chill,sir reddit,reddit ask me anything,rslash,toadfilms,r/,reddit funny,funny reddit,best of reddit,reddit compilation,reddit best"
    os.mkdir(rf'{cwd}\VIDEOS\{context["video_id"]}')
    os.rename(thumbnail_path, rf'{cwd}\VIDEOS\{context["video_id"]}\thumbnail.png')
    os.rename(video_path, rf'{cwd}\VIDEOS\{context["video_id"]}\video.mp4')
    with open(rf'{cwd}\VIDEOS\{context["video_id"]}\Video Info.txt','a') as file:
        file.writelines(f"TITLE:\n{post.title} [r/AskReddit] Reddit Stories\n\n\n")
        file.writelines(f"DESC:\n{description}\n\n\n")
        file.writelines(f'TAGS:\n{tags}\n\n\n')
        file.writelines(f'URL:\n{context["url"]}')
    paths = [
        rf'{cwd}\data\thumbnails\*.png',
        rf'{cwd}\data\video\*.mp4',
        rf'{cwd}\data\audio\*.mp3',
    ]

    for path in paths:
        files = glob.glob(path)
        for f in files:
            os.remove(f)

