from src.tasks.scrape_reddit.task import get_hottest_post
from src.tasks.text_to_speech.task import tts
from src.tasks.generate_video.task import generate_video
from src.tasks.upload_video.task import upload_video
from src.tasks.generate_thumbnail.task import generate_thumbnail
from src.tasks.cleanup.task import cleanup
import os

class Pipeline:
    def __init__(self):
        self.tasks = [
            get_hottest_post,
            tts,
            generate_video,
            generate_thumbnail,
            # upload_video,
            cleanup
        ]
        self.context = dict()

    def execute(self, **kwargs):
        self.context = kwargs
        for task in self.tasks:
            print(f"Current Task: {task.__name__}")
            task(self.context)
if __name__ == "__main__":
    # from time import sleep
    # sleep(3600)



    ############################## YOUTUBE

    # sa video do te renderizohen (nga videot me te mira te dites, mos u be merak se nuk perseriten)
    number_of_videos = 99
    # sa minuta e do videon
    video_minutes_limit = 11

    # sa komente do para se ti kujtosh te bejne like dhe subscribe
    comm_bef_likesub = 3
    # sa komente do para se ti kujtosh te bejne like dhe subscribe heren e dyte
    comm_bef_likesub2 = 9
    ##############################





    import json
    with open('past urls.json') as json_file:
        past_urls = json.load(json_file)

    pipeline = Pipeline()
    # URL e postimit ne reddit
    import praw

    urls = [
        "https://www.reddit.com/r/AskReddit/comments/ka5ncp/redditors_who_have_hired_a_private/",
    ]

    client_id = "iosCZqE9n_yFQw"
    client_secret = "Eu_vqISa7HWnPpWQmh6xcsDx36w"
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='YOUTUBE')

    # for post in reddit.subreddit('AskReddit').top('day'):
    #     if post.num_comments > 1000:
    #         if post.url not in past_urls['urls']:
    #             if len(urls) >= number_of_videos:
    #                 break
    #             urls.append(post.url)
    #
    #         else:
    #             print("Duplicate URL found. Skipping this one\n")
    # print(f"Found {len(urls)} posts\n")

    # Pak a shume sa minuta e do videon
    cwd = os.getcwd()

    for x,url in enumerate(urls):
        try:
            print(f"Trying URL nr {x+1}:\n{url}")
            pipeline.execute(url=url, video_minutes_limit=video_minutes_limit, cwd=cwd, comm_bef_likesub = comm_bef_likesub, comm_bef_likesub2=comm_bef_likesub2)
        except Exception as e:
            print(f'\n\n\n\n******************************\n{e}\n******************************\n\n\n\n')
        else:
            past_urls['urls'].append(url)
            with open('past urls.json', 'w') as json_file:
                json.dump(past_urls, json_file)
