# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photomagicapp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 160, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NegButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.NegButton.setObjectName("NegButton")
        self.verticalLayout.addWidget(self.NegButton)
        self.GrayButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.GrayButton.setObjectName("GrayButton")
        self.verticalLayout.addWidget(self.GrayButton)
        self.BWButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BWButton.setObjectName("BWButton")
        self.verticalLayout.addWidget(self.BWButton)
        self.ThreeDButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ThreeDButton.setObjectName("ThreeDButton")
        self.verticalLayout.addWidget(self.ThreeDButton)
        self.WNButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.WNButton.setObjectName("WNButton")
        self.verticalLayout.addWidget(self.WNButton)
        self.SaveChangesDialog = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.SaveChangesDialog.setGeometry(QtCore.QRect(210, 360, 166, 30))
        self.SaveChangesDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.SaveChangesDialog.setObjectName("SaveChangesDialog")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(240, 250, 111, 61))
        self.showButton.setObjectName("showButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 120, 239, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TurnLButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TurnLButton.setObjectName("TurnLButton")
        self.horizontalLayout.addWidget(self.TurnLButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.TurnRButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TurnRButton.setObjectName("TurnRButton")
        self.horizontalLayout.addWidget(self.TurnRButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 320, 181, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 68, 22))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MagicPhotoApp"))
        self.NegButton.setText(_translate("MainWindow", "Негатив"))
        self.GrayButton.setText(_translate("MainWindow", "Серое"))
        self.BWButton.setText(_translate("MainWindow", "Черно-белое"))
        self.ThreeDButton.setText(_translate("MainWindow", "3D"))
        self.WNButton.setText(_translate("MainWindow", "Белый шум"))
        self.showButton.setText(_translate("MainWindow", "Показать"))
        self.TurnLButton.setText(_translate("MainWindow", "влево"))
        self.TurnRButton.setText(_translate("MainWindow", "вправо"))
        self.label.setText(_translate("MainWindow", "Сохранить изменения?"))
        self.label_2.setText(_translate("MainWindow", "Поворот"))

