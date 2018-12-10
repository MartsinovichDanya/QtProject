import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow

class MainWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())
