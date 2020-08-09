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
            # generate_thumbnail,
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
    urls = [
        'https://www.reddit.com/r/AskReddit/comments/grst2b/police_officers_of_reddit_what_are_you_thinking/'
    ]
    # Pak a shume sa minuta e do videon
    video_minutes_limit = 13
    for url in urls:
        pipeline.execute(url=url, video_minutes_limit=video_minutes_limit)
