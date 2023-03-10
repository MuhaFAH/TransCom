# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ic/start.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 360)
        Dialog.setMinimumSize(QtCore.QSize(360, 360))
        Dialog.setMaximumSize(QtCore.QSize(360, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(27, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setMinimumSize(QtCore.QSize(36, 0))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("ic\\../pic/logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.your_name = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.your_name.setFont(font)
        self.your_name.setAlignment(QtCore.Qt.AlignCenter)
        self.your_name.setObjectName("your_name")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setText('Неверные данные')
        self.error.move(50, 320)
        self.error.setStyleSheet("color: red")
        self.error.setFont(font)
        self.error.resize(200, 30)
        self.error.hide()
        self.verticalLayout.addWidget(self.your_name)
        self.login = QtWidgets.QLineEdit(Dialog)
        self.login.setMinimumSize(QtCore.QSize(0, 25))
        self.login.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.your_password = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.your_password.setFont(font)
        self.your_password.setAlignment(QtCore.Qt.AlignCenter)
        self.your_password.setObjectName("your_password")
        self.verticalLayout.addWidget(self.your_password)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setMinimumSize(QtCore.QSize(0, 25))
        self.password.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.continue_btn = QtWidgets.QPushButton(Dialog)
        self.continue_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.continue_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.continue_btn.setTabletTracking(True)
        self.continue_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.continue_btn.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.continue_btn.setShortcut("")
        self.continue_btn.setObjectName("continue_btn")
        self.verticalLayout.addWidget(self.continue_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(27, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TransCom"))
        self.your_name.setText(_translate("Dialog", "Введите логин"))
        self.your_password.setText(_translate("Dialog", "Введите пароль"))
        self.continue_btn.setText(_translate("Dialog", "ОК"))
