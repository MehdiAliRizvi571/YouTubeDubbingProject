import yt_dlp
import os

def download_audio(urls):
    ydl_opts = {
        'format': 'bestaudio/best',        # grab highest quality audio track
        'outtmpl': '%(title)s.%(ext)s',    # filename = video title
        'cookiesfrombrowser': ('chrome',),  # or 'firefox', 'edge' — whatever you use
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',        # convert to WAV
            'preferredquality': '0',        # 0 = best quality (lossless for WAV)
        }],
        'postprocessor_args': [
            '-ar', '16000',                 # 16kHz sample rate (what Whisper wants)
            '-ac', '1',                     # mono channel (what Whisper wants)
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,                 # delete original after conversion
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

# ---- PASTE YOUR URLs HERE ----
urls = [
    "https://www.youtube.com/watch?v=aQSDSqdlFxk",
]

download_audio(urls)
print("✅ Done! WAV files saved in current folder.")