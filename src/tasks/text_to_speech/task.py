import uuid
import time
import requests
import random
from gtts import gTTS
from google.cloud import texttospeech_v1
import os
from src.tasks.generate_video.split_sentence import split_into_sentences


os.chdir('../')
cwd = os.getcwd()
os.chdir('src')

AUDIO_PATH = rf'{cwd}\data\audio'


def save_tts(text):
   return save_gtts(text)

def save_gtts(text):
   path = fr"{AUDIO_PATH}\{uuid.uuid4()}.mp3"
   save_wavenet(text, path)
   return path

def tts(context):
   post = context["post"]
   post.title_audio = save_tts(post.title)
   for comment in post.comments:
      comment.body_audio = []
      comment.text_list = split_into_sentences(comment.body)
      for sentence in comment.text_list:
         comment.body_audio.append(save_tts(sentence))
      # comment.body_audio = save_tts(comment.body)
      # if comment.reply:
      #    comment.reply_audio = save_tts(comment.reply)
   return


def save_wavenet(text, path):
   os.environ[
      "GOOGLE_APPLICATION_CREDENTIALS"] = rf"{cwd}\assets\Google Wavenet TTS-6c537e35e7ed.json"
   client = texttospeech_v1.TextToSpeechClient()
   synthesis_input = texttospeech_v1.types.SynthesisInput(text=text)
   voice = texttospeech_v1.types.VoiceSelectionParams(
      language_code='en-US',
      name='en-US-Wavenet-D',
      ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE)
   audio_config = texttospeech_v1.types.AudioConfig(
      audio_encoding=texttospeech_v1.AudioEncoding.MP3, speaking_rate=1.2, pitch=3.5)
   response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
   with open(path, 'wb') as out:
      # Write the response to the output file.
      out.write(response.audio_content)
   return

if __name__ == "__main__":
   save_tts(r"The internet is scheduled to go down forever. You have a week to prepare and download anything from the web you think is necessary to have for the rest of your life. What do you download and why?")
