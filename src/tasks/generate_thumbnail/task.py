from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap,fill

font = ImageFont.truetype(r'C:\Users\Olsi\PycharmProjects\kot\assets\D-DIN-Bold.otf', size=90)
WRAP_WIDTH = 18
TEXT_OFFSET = (90, 90)
BCKG_IMAGE = Image.open(r'C:\Users\Olsi\PycharmProjects\kot\assets\background1.png')
SIMPSON_IMAGE = Image.open(r'C:\Users\Olsi\PycharmProjects\kot\assets\homer.png')
THUMBNAIL_DIR = r"C:\Users\Olsi\PycharmProjects\kot\data\thumbnails"


def generate_thumbnail(context):
    post = context["post"]
    IMAGE_TEXT = post.title

    def find_highlight_text(txt):
        for text in wrap(IMAGE_TEXT,width=1, break_long_words=False):
            if len(text) > 8:
                return text
        for text in wrap(IMAGE_TEXT,width=1, break_long_words=False):
            if len(text) > 7:
                return text
        for text in wrap(IMAGE_TEXT,width=1, break_long_words=False):
            if len(text) > 6:
                return text
    def find_text_location(text, width, highlight_text, font):
        """ Returns a tuple of (height,width) of where the text should be in pixels on the image in relation to the text itself,
            text=whole text,
            width = width of the text wraper in number of characters per line,
            highlight_text = text to be found the location of"""
        wrapped_text = wrap(text, width=width, break_long_words=False)
        for line in enumerate(wrapped_text):
            if line[1].find(highlight_text) != -1:
                # highlight_text_start = (line[0], line[1].find(highlight_text))
                width1 = font.getsize(line[1][:line[1].find(highlight_text)])[0]
                height1 = font.getsize('a')[1] * line[0] + line[0]*4
                # im = Image.new("RGB", (600, 600))
                # draw = ImageDraw.Draw(im)
                # new_text = ''
                # for text in wrapped_text:
                #     if wrapped_text.index(text) > line[0]:
                #         break
                #     else:
                #         new_text += f'\n{text}'
                # draw.text((0, 0), new_text, font=font)
                # im = im.crop(im.getbbox())
                # text_height_end = im.size[1]
                # height1 = text_height_end - font.getsize('a')[1]
                position = (width1,height1)
                return position
    def rectangle_below_text(position,font, highlighted_text):
        """position of the text, font of the text and the actual text"""
        width = font.getsize(highlighted_text)[0]
        height = font.getsize(highlighted_text)[1]
        separator = font.getsize('a')[1] / 6
        draw.rectangle(((position[0]-separator,position[1]),(position[0]+width+separator, position[1]+height+separator)), fill='white')
        draw.text(position, highlighted_text, font=font, fill='black')


    thumbnail = Image.new("RGB", (1280, 720), (255, 255, 255))
    thumbnail.paste(BCKG_IMAGE)
    thumbnail.paste(SIMPSON_IMAGE,(777,21),SIMPSON_IMAGE)
    highlighted_text = find_highlight_text(IMAGE_TEXT)
    highlighted_text_position1 = find_text_location(text=IMAGE_TEXT,width=WRAP_WIDTH,highlight_text=highlighted_text, font=font)

    print(highlighted_text_position1)
    print(IMAGE_TEXT)

    draw = ImageDraw.Draw(thumbnail)
    highlighted_text_position = (highlighted_text_position1[0]+TEXT_OFFSET[0],highlighted_text_position1[1]+TEXT_OFFSET[1])
    rectangle_below_text(highlighted_text_position, font, highlighted_text)
    draw.text(TEXT_OFFSET,fill(IMAGE_TEXT, width=WRAP_WIDTH), font=font, fill='black')

    thumbnail.show()
    video_id = context["video_id"]
    thumbnail_path = fr"{THUMBNAIL_DIR}\{video_id}.png"
    thumbnail.save(thumbnail_path)
    context["thumbnail_path"] = thumbnail_path



