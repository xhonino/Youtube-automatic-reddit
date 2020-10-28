import textwrap
import uuid
from moviepy.editor import *
import os

os.chdir('../')
cwd = os.getcwd()
os.chdir('src')

TITLE_FONT_SIZE = 45
FONT_SIZE = 45
TITLE_FONT_COLOR = 'white'
BGM_PATH = rf'{cwd}\assets\bgm.mp3'
STATIC_PATH = rf'{cwd}\assets\static.mp4'
SIZE = (1920, 1080)
BG_COLOR = (16,16,16)
VIDEO_PATH = rf'{cwd}\data\video'
FONT = 'Calibri'
BACKGROUND_IMAGE = rf'{cwd}\assets\background_image.jpg'
LIKEANDSUB_CLIP1 = rf'{cwd}\assets\like_sub1.mp4'
LIKEANDSUB_CLIP2 = rf'{cwd}\assets\like_sub2.mp4'
END_SCREEN_CLIP = rf'{cwd}\assets\end_screen.mp4'
ARROW_IMAGE = rf'{cwd}\assets\Arrows.jpg'

def generate_title(text, audio_path):
    background_clip = ImageClip(BACKGROUND_IMAGE)
    audio_clip = AudioFileClip(audio_path)
    font_size = TITLE_FONT_SIZE
    wrapped_text = textwrap.fill(text, width=80)
    txt_clip = TextClip(wrapped_text,fontsize=font_size, font=FONT, color=TITLE_FONT_COLOR, align="west")
    txt_clip = txt_clip.set_position("center")
    clip = CompositeVideoClip([background_clip, txt_clip])
    clip.audio = audio_clip
    clip.duration = audio_clip.duration
    static_clip = VideoFileClip(STATIC_PATH)
    clip = concatenate_videoclips([clip, static_clip])
    return clip

def generate_clip(post, comment):
    text = comment.body
    audio_path = comment.body_audio


    background_clip = ImageClip(BACKGROUND_IMAGE)
    audio_clip = AudioFileClip(audio_path)
    font_size = TITLE_FONT_SIZE
    # author_font_size = 30
    wrapped_text = textwrap.fill(text, width=80)
    wrapped_wrap = len(textwrap.wrap(text, width=80))/2


    txt_clip = TextClip(wrapped_text,fontsize=font_size, font=FONT, color=TITLE_FONT_COLOR, align="west", interline=2)
    txt_clip_pos = (215, 525-wrapped_wrap*45)
    txt_clip = txt_clip.set_position(txt_clip_pos)

    # author_clip = TextClip(f"/u/{comment.author}", fontsize=author_font_size, font=FONT, color="lightblue")
    # author_pos = (SIZE[0]/2 - txt_clip.size[0]/2, SIZE[1]/2 - txt_clip.size[1]/2 - author_font_size - 15)
    # author_clip = author_clip.set_position(author_pos)
    #
    # score_clip = TextClip(f"{comment.score} points", fontsize=author_font_size, font=FONT, color="grey")
    # score_pos = (author_pos[0] + author_clip.size[0] + 30, author_pos[1])
    # score_clip = score_clip.set_position(score_pos)

    # arrow_clip = ImageClip(ARROW_IMAGE)
    # arrow_pos2 = 500-wrapped_wrap*45
    # arrow_pos1 = 110
    # arrow_pos = (arrow_pos1,arrow_pos2)
    # arrow_clip = arrow_clip.set_position(arrow_pos)

    arrow_clip = ImageClip(ARROW_IMAGE)
    arrow_pos = (txt_clip_pos[0]-arrow_clip.size[0]-25, txt_clip_pos[1]-35)
    arrow_clip = arrow_clip.set_position(arrow_pos)


    clip = CompositeVideoClip([background_clip, txt_clip, arrow_clip])
    clip.audio = audio_clip
    clip.duration = audio_clip.duration
    static_clip = VideoFileClip(STATIC_PATH)
    clip = concatenate_videoclips([clip, static_clip])
    return clip

def generate_video(context):
    comm_bef_likesub = context['comm_bef_likesub']
    comm_bef_likesub2 = context['comm_bef_likesub2']
    likeandsub_clip1 = VideoFileClip(LIKEANDSUB_CLIP1)
    likeandsub_clip2 = VideoFileClip(LIKEANDSUB_CLIP2)
    end_screen_clip = VideoFileClip(END_SCREEN_CLIP)
    static_clip = VideoFileClip(STATIC_PATH)
    post = context["post"]
    clips = []
    clips.append(generate_title(post.title, post.title_audio))
    for comment in post.comments:
        comment_clip = generate_clip(post, comment)
        # overlay reply
        if comment.reply:
            # TODO this
            pass
        clips.append(comment_clip)
        if len(clips)-1 == comm_bef_likesub:
            clips.append(likeandsub_clip1)
            clips.append(static_clip)
        if len(clips)-3 == comm_bef_likesub2:
            clips.append(likeandsub_clip2)
            clips.append(static_clip)
    clips.append(end_screen_clip)

    video = concatenate_videoclips(clips)
    background_audio_clip = AudioFileClip(BGM_PATH)
    background_audio_clip = afx.audio_loop(background_audio_clip, duration=video.duration)
    background_audio_clip = background_audio_clip.fx(afx.volumex, 0.1)
    video.audio = CompositeAudioClip([video.audio, background_audio_clip])
    video_id = uuid.uuid4()
    path = fr"{VIDEO_PATH}\{video_id}.mp4"
    context["video_path"] = path
    context["video_id"] = video_id
    video.write_videofile(path, fps=24, codec='libx264',bitrate='6291456', threads=4)

