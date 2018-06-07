from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save Location")

        progress.setValue(0)
        progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")

        download.clicked.connect(self.download)


    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()