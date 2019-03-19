import youtube_dl

youtube_download_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/hyakk/Desktop/Playlist/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

url = input("Paste URL Here: ")
with youtube_dl.YoutubeDL(youtube_download_opts) as y_dl:
    y_dl.download([url])
