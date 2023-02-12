# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ic\remTrans.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_remTrans(object):
    def setupUi(self, remTrans):
        remTrans.setObjectName("remTrans")
        remTrans.resize(500, 240)
        remTrans.setMinimumSize(QtCore.QSize(500, 240))
        remTrans.setMaximumSize(QtCore.QSize(500, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remTrans.setWindowIcon(icon)
        remTrans.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(remTrans)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.micrologo4 = QtWidgets.QLabel(remTrans)
        self.micrologo4.setMinimumSize(QtCore.QSize(30, 30))
        self.micrologo4.setMaximumSize(QtCore.QSize(30, 30))
        self.micrologo4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.micrologo4.setText("")
        self.micrologo4.setPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"))
        self.micrologo4.setAlignment(QtCore.Qt.AlignCenter)
        self.micrologo4.setObjectName("micrologo4")
        self.horizontalLayout_5.addWidget(self.micrologo4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.RemNewTransText = QtWidgets.QLabel(remTrans)
        self.RemNewTransText.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.RemNewTransText.setFont(font)
        self.RemNewTransText.setStyleSheet("background-color: \'white\';\n"
"color: rgb(255, 0, 0);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.RemNewTransText.setObjectName("RemNewTransText")
        self.horizontalLayout_4.addWidget(self.RemNewTransText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectTrans = QtWidgets.QLabel(remTrans)
        self.selectTrans.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.selectTrans.setFont(font)
        self.selectTrans.setAlignment(QtCore.Qt.AlignCenter)
        self.selectTrans.setObjectName("selectTrans")
        self.verticalLayout_2.addWidget(self.selectTrans)
        self.selectRemTrans = QtWidgets.QComboBox(remTrans)
        self.selectRemTrans.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectRemTrans.setFont(font)
        self.selectRemTrans.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.selectRemTrans.setObjectName("selectRemTrans")
        self.verticalLayout_2.addWidget(self.selectRemTrans)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.error = QtWidgets.QLabel(remTrans)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("color: rgb(170, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.horizontalLayout_7.addWidget(self.error)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.acceptButton = QtWidgets.QPushButton(remTrans)
        self.acceptButton.setMinimumSize(QtCore.QSize(0, 30))
        self.acceptButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.acceptButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout_7.addWidget(self.acceptButton)
        self.rejectButton = QtWidgets.QPushButton(remTrans)
        self.rejectButton.setMinimumSize(QtCore.QSize(0, 30))
        self.rejectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rejectButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.rejectButton.setObjectName("rejectButton")
        self.horizontalLayout_7.addWidget(self.rejectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(remTrans)
        QtCore.QMetaObject.connectSlotsByName(remTrans)

    def retranslateUi(self, remTrans):
        _translate = QtCore.QCoreApplication.translate
        remTrans.setWindowTitle(_translate("remTrans", "TransCom - удаление транспорта"))
        self.RemNewTransText.setText(_translate("remTrans", "Удаление транспорта"))
        self.selectTrans.setText(_translate("remTrans", "Выберите транспорт, который хотите убрать"))
        self.acceptButton.setText(_translate("remTrans", "Подтвердить"))
        self.rejectButton.setText(_translate("remTrans", "Отменить"))