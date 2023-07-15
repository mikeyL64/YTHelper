import yt_dlp

URL = ['https://www.youtube.com/playlist?list=PLRoc5AGAM63V_QxEU7vl--P3ZNeeg-0Pg']

ydl_opts = {
    "format": "bestaudio[ext*=4]/bestaudio[ext=mp3]/best[ext=mp4]/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio", 
        "preferredcodec": "m4a"
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URL)