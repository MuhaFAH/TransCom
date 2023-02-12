# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ic\RedactTrans.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RedactTrans(object):
    def setupUi(self, RedactTrans):
        RedactTrans.setObjectName("RedactTrans")
        RedactTrans.resize(580, 320)
        RedactTrans.setMinimumSize(QtCore.QSize(580, 320))
        RedactTrans.setMaximumSize(QtCore.QSize(580, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RedactTrans.setWindowIcon(icon)
        RedactTrans.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(RedactTrans)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.micrologo5 = QtWidgets.QLabel(RedactTrans)
        self.micrologo5.setMinimumSize(QtCore.QSize(30, 30))
        self.micrologo5.setMaximumSize(QtCore.QSize(30, 30))
        self.micrologo5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.micrologo5.setText("")
        self.micrologo5.setPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"))
        self.micrologo5.setAlignment(QtCore.Qt.AlignCenter)
        self.micrologo5.setObjectName("micrologo5")
        self.horizontalLayout_5.addWidget(self.micrologo5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.RedactTransText = QtWidgets.QLabel(RedactTrans)
        self.RedactTransText.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.RedactTransText.setFont(font)
        self.RedactTransText.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.RedactTransText.setObjectName("RedactTransText")
        self.horizontalLayout_4.addWidget(self.RedactTransText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectedTrans = QtWidgets.QLabel(RedactTrans)
        self.selectedTrans.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.selectedTrans.setFont(font)
        self.selectedTrans.setAlignment(QtCore.Qt.AlignCenter)
        self.selectedTrans.setObjectName("selectedTrans")
        self.verticalLayout_2.addWidget(self.selectedTrans)
        self.selectRedactTrans = QtWidgets.QComboBox(RedactTrans)
        self.selectRedactTrans.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectRedactTrans.setFont(font)
        self.selectRedactTrans.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.selectRedactTrans.setObjectName("selectRedactTrans")
        self.verticalLayout_2.addWidget(self.selectRedactTrans)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.howRedactModelName = QtWidgets.QLabel(RedactTrans)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.howRedactModelName.setFont(font)
        self.howRedactModelName.setStyleSheet("")
        self.howRedactModelName.setObjectName("howRedactModelName")
        self.horizontalLayout.addWidget(self.howRedactModelName)
        self.newModelName = QtWidgets.QLineEdit(RedactTrans)
        self.newModelName.setMinimumSize(QtCore.QSize(0, 30))
        self.newModelName.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.newModelName.setObjectName("newModelName")
        self.horizontalLayout.addWidget(self.newModelName)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.howRedactTonnage = QtWidgets.QLabel(RedactTrans)
        self.howRedactTonnage.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.howRedactTonnage.setFont(font)
        self.howRedactTonnage.setStyleSheet("")
        self.howRedactTonnage.setObjectName("howRedactTonnage")
        self.horizontalLayout_2.addWidget(self.howRedactTonnage)
        self.newTonnage = QtWidgets.QDoubleSpinBox(RedactTrans)
        self.newTonnage.setMinimumSize(QtCore.QSize(0, 30))
        self.newTonnage.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.newTonnage.setObjectName("newTonnage")
        self.horizontalLayout_2.addWidget(self.newTonnage)
        self.tons = QtWidgets.QLabel(RedactTrans)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.tons.setFont(font)
        self.tons.setObjectName("tons")
        self.horizontalLayout_2.addWidget(self.tons)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gosznakRedactText = QtWidgets.QLabel(RedactTrans)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.gosznakRedactText.setFont(font)
        self.gosznakRedactText.setStyleSheet("")
        self.gosznakRedactText.setObjectName("gosznakRedactText")
        self.horizontalLayout_3.addWidget(self.gosznakRedactText)
        self.newCarNumber = QtWidgets.QLineEdit(RedactTrans)
        self.newCarNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.newCarNumber.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.newCarNumber.setObjectName("newCarNumber")
        self.horizontalLayout_3.addWidget(self.newCarNumber)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.error = QtWidgets.QLabel(RedactTrans)
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
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.acceptButton = QtWidgets.QPushButton(RedactTrans)
        self.acceptButton.setMinimumSize(QtCore.QSize(0, 30))
        self.acceptButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.acceptButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout_7.addWidget(self.acceptButton)
        self.rejectButton = QtWidgets.QPushButton(RedactTrans)
        self.rejectButton.setMinimumSize(QtCore.QSize(0, 30))
        self.rejectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rejectButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.rejectButton.setObjectName("rejectButton")
        self.horizontalLayout_7.addWidget(self.rejectButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.retranslateUi(RedactTrans)
        QtCore.QMetaObject.connectSlotsByName(RedactTrans)

    def retranslateUi(self, RedactTrans):
        _translate = QtCore.QCoreApplication.translate
        RedactTrans.setWindowTitle(_translate("RedactTrans", "TransCom - редактирование"))
        self.RedactTransText.setText(_translate("RedactTrans", "Редактирование информации"))
        self.selectedTrans.setText(_translate("RedactTrans", "Выберите изменяемый транспорт:"))
        self.howRedactModelName.setText(_translate("RedactTrans", "Название модели:"))
        self.howRedactTonnage.setText(_translate("RedactTrans", "Грузоподъёмность модели:"))
        self.tons.setText(_translate("RedactTrans", "тонн"))
        self.gosznakRedactText.setText(_translate("RedactTrans", "Актуальный номерной знак:"))
        self.acceptButton.setText(_translate("RedactTrans", "Подтвердить"))
        self.rejectButton.setText(_translate("RedactTrans", "Отменить"))
