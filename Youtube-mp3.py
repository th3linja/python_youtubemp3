import sys
import youtube_dl
from PyQt5 import QtWidgets
from collections import deque
import threading
import os


# os.system("cmd /c python -m pip install --upgrade pip")
# os.system("cmd /c pip install --upgrade youtube_dl")
# os.system("cmd /c pip install --upgrade PyQt5")


class YoutubeMP3(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.youtube_download_opts = {
            'skip_download': True,
            'outtmpl': 'C:/Users/hyakk/Desktop/Playlist/%(title)s.%(ext)s',
        }
        self.add = QtWidgets.QPushButton("Add")
        self.download = QtWidgets.QPushButton("Download")
        self.line_add = QtWidgets.QLineEdit()
        self.edit = QtWidgets.QPushButton("Edit")
        self.thumbnail = QtWidgets.QLabel()
        self.queue = deque()
        self.title = deque()
        self.gui_title = QtWidgets.QLabel("")
        self.gui_list = QtWidgets.QLabel("")
        self.temp = ""

        h1_box = QtWidgets.QHBoxLayout()
        h1_box.addWidget(self.gui_list)

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addStretch()
        h2_box.addWidget(self.add)
        h2_box.addWidget(self.download)
        h2_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.line_add)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("Youtube MP3")
        self.setGeometry(300, 300, 400, 100)
        self.download.clicked.connect(self.download_btn)
        self.add.clicked.connect(self.add_btn)
        self.show()

    def download_btn(self):
        sender = self.sender()
        re_download_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'C:/Users/hyakk/Desktop/Playlist/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        if sender.text() == "Download":
            with youtube_dl.YoutubeDL(re_download_opts) as y_dl:
                while len(self.queue) > 0:
                    y_dl.download([self.queue.popleft()])
                self.gui_list.setText("Download Completed")

    def add_btn(self):
        sender = self.sender()
        if sender.text() == "Add":
            if self.line_add.text().strip(" ") in self.queue:
                print("This is already in queue.")
                self.line_add.clear()
            elif self.line_add.text().strip(" ") == "":
                print("Please enter a valid URL")
            else:
                self.gui_title.setText(youtube_dl.YoutubeDL(self.youtube_download_opts)
                                       .extract_info(self.line_add.text().strip(" "), download=False)['title'])
                self.temp += str(self.gui_title.text() + '\n' + self.line_add.text().strip(" ")) + '\n'
                self.gui_list.setText(self.temp)
                self.queue.append(str(self.line_add.text().strip(" ")))
                self.title.append(self.gui_title.text().translate(self.gui_title.text().maketrans('\/:*?"<>|', '_________')))
                self.line_add.clear()
                print(self.queue)
                print(self.title)

    def edit_btn(self):
        sender = self.sender()
        if sender.text() == "Edit":
            return


sys.except_hook = sys.excepthook


def my_exception_hook(exc_type, value, traceback):
    print(exc_type, value, traceback)
    sys.except_hook(exc_type, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook


app = QtWidgets.QApplication(sys.argv)
a_window = YoutubeMP3()
sys.exit(app.exec_())




