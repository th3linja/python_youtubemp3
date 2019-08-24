import youtube_dl
import os

os.system("cmd /c python -m pip install --upgrade pip")
os.system("cmd /c pip install --upgrade youtube_dl")


def music_download():
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


cont = "y"
while cont == "y":
    music_download()
    cont = input("Do you wish to continue? (y/n) ")
    while cont != "y" and cont != "n":
        cont = input("Please enter a valid input. (y/n) ")
