import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QInputDialog
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QMessageBox, QErrorMessage
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow
import shutil
import os.path
from time import sleep


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

    def show_pic(self):
        self.pic = Picture()


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
