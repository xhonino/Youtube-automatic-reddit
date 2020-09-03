from src.tasks.scrape_reddit.task import get_hottest_post
from src.tasks.text_to_speech.task import tts
from src.tasks.generate_video.task import generate_video
from src.tasks.upload_video.task import upload_video
from src.tasks.generate_thumbnail.task import generate_thumbnail
from src.tasks.cleanup.task import cleanup

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
    pipeline = Pipeline()
    # URL e postimit ne reddit
    import praw
    urls = []
    client_id = "iosCZqE9n_yFQw"
    client_secret = "Eu_vqISa7HWnPpWQmh6xcsDx36w"
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='YOUTUBE')
    for post in reddit.subreddit('AskReddit').top('day'):
        if post.score > 10000 and post.title.__len__() < 100:
            urls.append(post.url)
            print(post.url)
            break
    # Pak a shume sa minuta e do videon
    video_minutes_limit = 0.05
    for url in urls:
        try:
            pipeline.execute(url=url, video_minutes_limit=video_minutes_limit)
        except Exception as e:
            print(f'\n\n\n\n**********    {e}    **********\n\n\n\n')