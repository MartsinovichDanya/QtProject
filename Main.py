import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QInputDialog
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from photomagicapp import Ui_MainWindow

class MainWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex = MainWidget()
ex.name, okBtnPressed = QInputDialog.getText(
            ex, "Имя файла", "имя"
        )
if not okBtnPressed:
    sys.exit()
ex.show()
sys.exit(app.exec_())
