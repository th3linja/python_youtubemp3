# python_youtubemp3
Using ffmpeg and youtube-dl to download audio files -> convert to mp3 and create a personal playlist.

## Getting Started
The purpose of this project is to create a simple and convenient method of downloading the audio files from a Youtube video and converting that file into a playlist standard `.mp3` file. Rather than relying on online converters, this project gives much more personal experience and creativity when creating one's playlist. This project is not intended to disregard any original content on Youtube but allow the public to have access to that material - with all respect to the creators and following legal usage.

**This project was originally built/intended for Window/OS users. Linux and Mac users will have varying and different steps that can be found online.**

When everything is done installing, open `Youtube-mp3.py` with any suitable IDE (IDLE, PyCharm, etc.). Edit the file location in `outtmpl` under `youtube_download_opts` by replacing `C:/Users/hyakk/Desktop/Playlist/` with any location of your own. This is where the downloaded audio files will go.

Run the program and paste the link of a youtube video into the URL prompt. **Add a space before pressing `ENTER` (otherwise you may end up opening the same link in a different tab on your browser).** The program should run if everything is done correctly and you should see a `.mp3` under the file location of where you indicated in `outtmpl`.

## Prequisites
  * Python
  * ffmpeg
  * youtube-dl
  
## Installing
Head over to [Python.org](https://www.python.org/) to download the latest version of Python if you haven't already. Make sure to enable pip in  `Optional Features` when installing. After installing, head over to Advanced System Settings -> Environment Variables and add Python into PATH. Open the command prompt (cmd) and run the command `pip3 install youtube-dl`.

If you do not have `ffmpeg` downloaded, you can head to this [link](https://www.ffmpeg.org/download.html) to download it. **Add `ffmpeg` into PATH (specifically the bin folder containing the three `EXE`'s: _ffmpeg_, _ffplay_, and _ffprobe_)**. Keep in mind that I will have a version of `ffmpeg` available in this project.

Download this project folder, which will contain both `ffmpeg` and `Youtube-mp3.py`.

## Running Tests
Make sure `youtube-dl` is up to date by running `pip3 install --upgrade youtube-dl`.
Make sure `ffmpeg` is in the same directory as your working folder.
Change the file path in `Youtube-mp3.py` (refer to **Getting Started**).
Make sure that `ffmpeg` and `Youtube-mp3.py` is in the same working directory.
Make sure `ffmpeg` is added in PATH under Environment Variables.

## Built With
  * Python
  * ffmpeg
  * youtube-dl
  
## Authors
th3linja

## Acknowledgments
All credit goes to developers and community for creating an amazing library available for public use. Youtube-dl also supports many other sites and this list can be found on their page in the link below.
  * [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)
  * [ffmpeg](https://www.ffmpeg.org/)
