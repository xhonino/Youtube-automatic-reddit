import praw
import os
from time import sleep
from praw.models import MoreComments
from src.tasks.scrape_reddit.post import Post, Comment
from src.tasks.scrape_reddit.profanity_filter import filter

client_id = "iosCZqE9n_yFQw"
client_secret = "Eu_vqISa7HWnPpWQmh6xcsDx36w"

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='YOUTUBE')

def get_hottest_post(context):
   video_minutes_limit = context["video_minutes_limit"]
   post = reddit.submission(url=context["url"])
   comments = []
   post.comments.replace_more(limit=1)
   total_characters = 0 ### ### ### ####  Duhet per kontrollin e gjatesise se videos
   for comment in post.comments:
      if comment.body == '[deleted]':
         continue
      if len(comment.body) > 1500:
         continue
      if comment.stickied:
         continue
      if comment.body.find("https:") != -1 or comment.body.find("http:") != -1 or comment.body.find("www.") != -1:
         continue
      comment_body = filter(comment.body)
      if comment_body == "[removed]":
         continue
      comment_reply = ""
      comment.replies.replace_more(limit=1)
      if len(comment.replies) > 0:
         reply = comment.replies[0]
         if isinstance(reply, MoreComments):
            continue
         comment_reply = filter(reply.body)
      comment_output = Comment(comment_body, comment_reply)
      if comment.author is not None:
         comment_output.author = comment.author.name
      else:
         comment_output.author = '[deleted]'
      comment_output.score = comment.score
      comments.append(comment_output)

      ############### Kontroll per gjatesine e videos ##################
      total_characters += len(comment_body)
      video_minutes = total_characters/850
      # sleep(5)
      if video_minutes >= video_minutes_limit:
         break

   post.title = filter(post.title)

   post_data = Post(post.title, comments)
   post_data.score = post.score
   post_data.num_comments = post.num_comments
   context["post"] = post_data
   return

   ############## OLD CODE ##################
   # subreddit_name=context["subreddit"]
   # comment_limit=context["comment_limit"]
   # nsfw=context["nsfw"]
   # subreddit = reddit.subreddit(subreddit_name)
   # hot_posts = subreddit.hot()
   # for post in hot_posts:
   #    if not post.stickied and post.over_18 == nsfw:
   #       title = post.title
   #       if len(title) >= 100:
   #          continue # respect youtube limit of 100
   #       comments = []
   #       for comment in post.comments:
   #          if isinstance(comment, MoreComments):
   #             continue
   #          if comment.stickied:
   #             continue
   #          comment_body = comment.body
   #          if comment_body == "[removed]":
   #             continue
   #          comment_reply = ""
   #          comment.replies.replace_more(limit=1)
   #          if len(comment.replies) > 0:
   #             reply = comment.replies[0]
   #             if isinstance(reply, MoreComments):
   #                continue
   #             comment_reply = reply.body
   #          comment_output = Comment(comment_body, comment_reply)
   #          comment_output.author = comment.author.name
   #          comment_output.score = comment.score
   #          comments.append(comment_output)
   #          if len(comments) >= comment_limit:
   #             break
   #
   #       post_data = Post(title, comments)
   #       post_data.score = post.score
   #       post_data.num_comments = post.num_comments
   #       context["post"] = post_data
   #       return
   ############## OLD CODE ##################

if __name__ == '__main__':
   url = 'https://www.reddit.com/r/AskReddit/comments/i3ntz9/what_is_the_worst_feeling_emotionally_in_your/'
   context= {'url':url, 'video_minutes_limit': 3, "post":None}
   get_hottest_post(context)
