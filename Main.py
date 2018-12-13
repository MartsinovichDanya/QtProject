import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QInputDialog
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QMessageBox, QErrorMessage
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow
import shutil
import os.path
from cbimg import gray
from negativ import neg
from noise import noise
from threeDAnagliph import makeanagliph


class Picture(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Просмотр')
        self.hbox = QHBoxLayout(self)
        self.pixmap = QPixmap('img.jpg')
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

    def show_pic(self):
        self.pic = Picture()

    def mk_gray(self):
        self.StatusLabel.hide()
        gray('img.jpg')
        self.StatusLabel.show()

    def mk_neg(self):
        self.StatusLabel.hide()
        neg('img.jpg')
        self.StatusLabel.show()

    def mk_noise(self):
        self.StatusLabel.hide()
        noise('img.jpg')
        self.StatusLabel.show()

    def mk_threeD(self):
        self.StatusLabel.hide()
        makeanagliph('img.jpg')
        self.StatusLabel.show()


app = QApplication(sys.argv)
ex = MainWidget()
name, okBtnPressed = QInputDialog.getText(
            ex, "Имя файла", "Имя файла"
        )
if not okBtnPressed:
    sys.exit()
if os.path.exists(name):
    shutil.copy(name, 'img.jpg')
    ex.show()
else:
    error_dialog = QErrorMessage()
    error_dialog.showMessage('Файл не найден!!!')
    error_dialog.setWindowTitle('Ошибка!')
sys.exit(app.exec_())
