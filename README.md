# Youtube and Tiktok Video Creator
Automatically create Youtube or Tiktok videos from Reddit Posts. Everything is automatic, you just need to start the script and provide how many videos you need. The script will deal with the rest.
<ol>
    <li>Collects best posts on reddit and its comments.</li>
    <li>Creates audio from the comments with google cloud tts API.</li>
    <li>Creates a thumbnail with Pillow.</li>
    <li>Bulit in profanity filter to avoid getting demonetized on youtube due to profanity.</li>
    <li>Creates the video and saves it in a local folder. </li>
</ol>	
  
## Stack used:
<ul>
    <li><strong>Reddit API</strong> to collect best posts from reddit.</li>
    <li><strong>Moviepy</strong> for the video creation.</li>
    <li><strong>Google Cloud TTS API</strong> for reading the comments.</li>
    <li><strong>Pillow</strong> for the thumbnail.</li>
    <li><strong>Regex</strong> for the profanity filter.</li>
</ul>
<h3><strong>SAMPLE</strong>: https://www.youtube.com/channel/UCbPl1jArnXnYf-xY__qA0hg</h3>

