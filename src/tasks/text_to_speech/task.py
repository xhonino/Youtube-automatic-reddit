import uuid
import time
import requests
import random
from gtts import gTTS
from google.cloud import texttospeech_v1
import os

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
      comment.body_audio = save_tts(comment.body)
      if comment.reply:
         comment.reply_audio = save_tts(comment.reply)
   return


def save_wavenet(text, path):
   os.environ[
      "GOOGLE_APPLICATION_CREDENTIALS"] = rf"{cwd}\assets\Google Wavenet TTS-6c537e35e7ed.json"
   client = texttospeech_v1.TextToSpeechClient()
   synthesis_input = texttospeech_v1.types.SynthesisInput(text=text)
   voice = texttospeech_v1.types.VoiceSelectionParams(
      language_code='en-US',
      name='en-US-Wavenet-F',
      ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE)
   audio_config = texttospeech_v1.types.AudioConfig(
      audio_encoding=texttospeech_v1.AudioEncoding.MP3)
   response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
   with open(path, 'wb') as out:
      # Write the response to the output file.
      out.write(response.audio_content)
   return

if __name__ == "__main__":
   save_tts("i am a potato, what are you?")
