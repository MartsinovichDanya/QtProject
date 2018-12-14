import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLabel, QErrorMessage, QHBoxLayout, QInputDialog
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow
import shutil
import os.path

import grayimg
import negativ
import noise
import threeDAnagliph
import bwimg


class Image:
    def __init__(self):
        self.last_op = ''
        self.name = 'img.jpg'


class Picture(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Просмотр')
        self.hbox = QHBoxLayout(self)
        self.pixmap = QPixmap(im.name)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        self.show()


class MainWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showButton.clicked.connect(self.show_pic)
        self.GrayButton.clicked.connect(self.mk_gray)
        self.NegButton.clicked.connect(self.mk_neg)
        self.WNButton.clicked.connect(self.mk_noise)
        self.ThreeDButton.clicked.connect(self.mk_threeD)
        self.BWButton.clicked.connect(self.mk_bw)
        self.BackButton.clicked.connect(self.back)

    def show_pic(self):
        self.pic = Picture()

    def mk_gray(self):
        self.StatusLabel.hide()
        grayimg.gray(im)
        self.StatusLabel.show()
        im.last_op = 'gray'

    def mk_neg(self):
        self.StatusLabel.hide()
        negativ.neg(im)
        self.StatusLabel.show()
        im.last_op = 'neg'

    def mk_noise(self):
        self.StatusLabel.hide()
        noise.noise(im)
        self.StatusLabel.show()
        im.last_op = 'noise'

    def mk_threeD(self):
        self.StatusLabel.hide()
        threeDAnagliph.makeanagliph(im)
        self.StatusLabel.show()
        im.last_op = '3d'

    def mk_bw(self):
        self.StatusLabel.hide()
        bwimg.bw(im)
        self.StatusLabel.show()
        im.last_op = 'bw'

    def back(self):
        if im.last_op == 'gray':
            grayimg.back(im)
        elif im.last_op == 'neg':
            negativ.back(im)
        elif im.last_op == '3d':
            threeDAnagliph.back(im)
        elif im.last_op == 'bw':
            bwimg.back(im)
        elif im.last_op == 'noise':
            noise.back(im)


app = QApplication(sys.argv)
ex = MainWidget()
name, okBtnPressed = QInputDialog.getText(
            ex, "Имя файла", "Имя файла"
        )
if not okBtnPressed:
    sys.exit()
if os.path.exists(name):
    im = Image()
    shutil.copy(name, im.name)
    ex.show()
else:
    error_dialog = QErrorMessage()
    error_dialog.showMessage('Файл не найден!!!')
    error_dialog.setWindowTitle('Ошибка!')
sys.exit(app.exec_())
