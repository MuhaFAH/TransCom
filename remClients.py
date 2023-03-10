# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ic\remClients.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_remClients(object):
    def setupUi(self, remClients):
        remClients.setObjectName("remClients")
        remClients.resize(410, 186)
        remClients.setMinimumSize(QtCore.QSize(410, 186))
        remClients.setMaximumSize(QtCore.QSize(410, 186))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remClients.setWindowIcon(icon)
        remClients.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(remClients)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.micrologo16 = QtWidgets.QLabel(remClients)
        self.micrologo16.setMinimumSize(QtCore.QSize(30, 30))
        self.micrologo16.setMaximumSize(QtCore.QSize(30, 30))
        self.micrologo16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.micrologo16.setText("")
        self.micrologo16.setPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"))
        self.micrologo16.setAlignment(QtCore.Qt.AlignCenter)
        self.micrologo16.setObjectName("micrologo16")
        self.horizontalLayout_5.addWidget(self.micrologo16)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.RemClientText = QtWidgets.QLabel(remClients)
        self.RemClientText.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.RemClientText.setFont(font)
        self.RemClientText.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"color: rgb(255, 0, 0);")
        self.RemClientText.setObjectName("RemClientText")
        self.horizontalLayout_4.addWidget(self.RemClientText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectClient = QtWidgets.QLabel(remClients)
        self.selectClient.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.selectClient.setFont(font)
        self.selectClient.setAlignment(QtCore.Qt.AlignCenter)
        self.selectClient.setObjectName("selectClient")
        self.verticalLayout_2.addWidget(self.selectClient)
        self.selectRemClients = QtWidgets.QComboBox(remClients)
        self.selectRemClients.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectRemClients.setFont(font)
        self.selectRemClients.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.selectRemClients.setObjectName("selectRemClients")
        self.verticalLayout_2.addWidget(self.selectRemClients)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.error = QtWidgets.QLabel(remClients)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("color: rgb(170, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")
        self.horizontalLayout_8.addWidget(self.error)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.acceptButton = QtWidgets.QPushButton(remClients)
        self.acceptButton.setMinimumSize(QtCore.QSize(0, 30))
        self.acceptButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.acceptButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout_8.addWidget(self.acceptButton)
        self.rejectButton = QtWidgets.QPushButton(remClients)
        self.rejectButton.setMinimumSize(QtCore.QSize(0, 30))
        self.rejectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rejectButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.rejectButton.setObjectName("rejectButton")
        self.horizontalLayout_8.addWidget(self.rejectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(remClients)
        QtCore.QMetaObject.connectSlotsByName(remClients)

    def retranslateUi(self, remClients):
        _translate = QtCore.QCoreApplication.translate
        remClients.setWindowTitle(_translate("remClients", "TransCom - ???????????????? ??????????????"))
        self.RemClientText.setText(_translate("remClients", "???????????????? ??????????????"))
        self.selectClient.setText(_translate("remClients", "???????????????? ??????????????, ???????????????? ???????????? ????????????"))
        self.acceptButton.setText(_translate("remClients", "??????????????????????"))
        self.rejectButton.setText(_translate("remClients", "????????????????"))
