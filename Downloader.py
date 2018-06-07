from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton()

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)



app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()