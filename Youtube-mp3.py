import sys
import youtube_dl
from PyQt5 import QtWidgets
from collections import deque
import os

os.system("cmd /c python -m pip install --upgrade pip")
os.system("cmd /c pip install --upgrade youtube_dl")
os.system("cmd /c pip install --upgrade PyQt5")
que = deque()


class YoutubeMP3(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):

        self.add = QtWidgets.QPushButton("Add")
        self.download = QtWidgets.QPushButton("Download")
        self.line = QtWidgets.QLineEdit()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.add)
        h_box.addWidget(self.download)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.line)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Youtube MP3")
        self.download.clicked.connect(self.btn_clicked)
        self.add.clicked.connect(self.btn_clicked)
        self.show()

    def btn_clicked(self):
        global que
        sender = self.sender()
        if sender.text() == "Download":
            youtube_download_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'C:/Users/hyakk/Desktop/Playlist/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with youtube_dl.YoutubeDL(youtube_download_opts) as y_dl:
                while not que:
                    y_dl.download([que.popleft()])

        if sender.text() == "Add":
            que.append(str(self.line.text()))
            self.line.clear()
            print(que)


sys.except_hook = sys.excepthook


def my_exception_hook(exc_type, value, traceback):
    print(exc_type, value, traceback)
    sys.except_hook(exc_type, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook


app = QtWidgets.QApplication(sys.argv)
a_window = YoutubeMP3()
sys.exit(app.exec_())




