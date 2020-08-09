import subprocess

def upload_video(context):
    post = context["post"]
    subreddit = context["subreddit"]
    video_path = context["video_path"]
    thumbnail_path = context["thumbnail_path"]
    title = post.title
    description = title + f" (/r/{subreddit})"

    args = (r"C:\Users\Olsi\PycharmProjects\kot\binyoutubeuploader_linux_amd64", "-filename", video_path, "-title", title, "-description", description,
            "-thumbnail", thumbnail_path, "-privacy", "public")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)

