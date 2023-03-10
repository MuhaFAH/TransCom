# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ic\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 681)
        MainWindow.setMinimumSize(QtCore.QSize(1043, 681))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Table = QtWidgets.QTabWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Table.setFont(font)
        self.Table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Table.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Table.setObjectName("Table")
        self.orders = QtWidgets.QWidget()
        self.orders.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.orders.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.orders.setObjectName("orders")
        self.gridLayout = QtWidgets.QGridLayout(self.orders)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.micrologo1 = QtWidgets.QLabel(self.orders)
        self.micrologo1.setMaximumSize(QtCore.QSize(30, 30))
        self.micrologo1.setText("")
        self.micrologo1.setPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"))
        self.micrologo1.setObjectName("micrologo1")
        self.horizontalLayout_2.addWidget(self.micrologo1)
        self.reportButton = QtWidgets.QPushButton(self.orders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportButton.sizePolicy().hasHeightForWidth())
        self.reportButton.setSizePolicy(sizePolicy)
        self.reportButton.setMinimumSize(QtCore.QSize(100, 30))
        self.reportButton.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.reportButton.setObjectName("reportButton")
        self.horizontalLayout_2.addWidget(self.reportButton)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.orders)
        self.add_btn.setMinimumSize(QtCore.QSize(480, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.free = QtWidgets.QLabel(self.orders)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.free.setFont(font)
        self.free.setStyleSheet("color: rgb(0, 170, 0);")
        self.free.setAlignment(QtCore.Qt.AlignCenter)
        self.free.setObjectName("free")
        self.verticalLayout.addWidget(self.free)
        self.free_tracks = QtWidgets.QTableWidget(self.orders)
        self.free_tracks.setStyleSheet("background-color: \'white\';\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.free_tracks.setObjectName("free_tracks")
        self.free_tracks.setColumnCount(3)
        self.free_tracks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.free_tracks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.free_tracks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.free_tracks.setHorizontalHeaderItem(2, item)
        self.free_tracks.horizontalHeader().setDefaultSectionSize(160)
        self.free_tracks.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.free_tracks)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.a_way = QtWidgets.QLabel(self.orders)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setItalic(False)
        self.a_way.setFont(font)
        self.a_way.setStyleSheet("color: rgb(255, 0, 0);")
        self.a_way.setAlignment(QtCore.Qt.AlignCenter)
        self.a_way.setObjectName("a_way")
        self.verticalLayout_2.addWidget(self.a_way)
        self.a_way_trucks = QtWidgets.QTableWidget(self.orders)
        self.a_way_trucks.setMinimumSize(QtCore.QSize(507, 500))
        self.a_way_trucks.setStyleSheet("background-color: \'white\';\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.a_way_trucks.setObjectName("a_way_trucks")
        self.a_way_trucks.setColumnCount(5)
        self.a_way_trucks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.a_way_trucks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.a_way_trucks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.a_way_trucks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.a_way_trucks.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.a_way_trucks.setHorizontalHeaderItem(4, item)
        self.a_way_trucks.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.a_way_trucks)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.control_trans_btn = QtWidgets.QPushButton(self.orders)
        self.control_trans_btn.setMinimumSize(QtCore.QSize(400, 30))
        self.control_trans_btn.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.control_trans_btn.setObjectName("control_trans_btn")
        self.horizontalLayout_6.addWidget(self.control_trans_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.Table.addTab(self.orders, "")
        self.clients = QtWidgets.QWidget()
        self.clients.setObjectName("clients")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.clients)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.micrologo2 = QtWidgets.QLabel(self.clients)
        self.micrologo2.setMaximumSize(QtCore.QSize(30, 30))
        self.micrologo2.setText("")
        self.micrologo2.setPixmap(QtGui.QPixmap("ic\\../pic/micrologo.png"))
        self.micrologo2.setObjectName("micrologo2")
        self.horizontalLayout_5.addWidget(self.micrologo2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.control_btn = QtWidgets.QPushButton(self.clients)
        self.control_btn.setMinimumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control_btn.setFont(font)
        self.control_btn.setStyleSheet("background-color: \'white\';\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.control_btn.setObjectName("control_btn")
        self.horizontalLayout_5.addWidget(self.control_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rating = QtWidgets.QLabel(self.clients)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rating.setFont(font)
        self.rating.setAlignment(QtCore.Qt.AlignCenter)
        self.rating.setObjectName("rating")
        self.verticalLayout_3.addWidget(self.rating)
        self.rating_table = QtWidgets.QTableWidget(self.clients)
        self.rating_table.setStyleSheet("background-color: \'white\';\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.rating_table.setObjectName("rating_table")
        self.rating_table.setColumnCount(2)
        self.rating_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.rating_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rating_table.setHorizontalHeaderItem(1, item)
        self.rating_table.horizontalHeader().setDefaultSectionSize(240)
        self.rating_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.rating_table)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.story = QtWidgets.QLabel(self.clients)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.story.setFont(font)
        self.story.setAlignment(QtCore.Qt.AlignCenter)
        self.story.setObjectName("story")
        self.verticalLayout_4.addWidget(self.story)
        self.choose_client = QtWidgets.QComboBox(self.clients)
        self.choose_client.setStyleSheet("background-color: \'white\';\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.choose_client.setObjectName("choose_client")
        self.verticalLayout_4.addWidget(self.choose_client)
        self.story_orders = QtWidgets.QTableWidget(self.clients)
        self.story_orders.setStyleSheet("background-color: \'white\';\n"
"border-radius: 2px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.story_orders.setObjectName("story_orders")
        self.story_orders.setColumnCount(4)
        self.story_orders.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.story_orders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.story_orders.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.story_orders.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.story_orders.setHorizontalHeaderItem(3, item)
        self.story_orders.horizontalHeader().setDefaultSectionSize(123)
        self.story_orders.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.story_orders)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.Table.addTab(self.clients, "")
        self.gridLayout_2.addWidget(self.Table, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.Table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TransCom"))
        self.reportButton.setText(_translate("MainWindow", "??????????"))
        self.add_btn.setText(_translate("MainWindow", "???????????????? ?????????? ??????????"))
        self.free.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        item = self.free_tracks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????????????????"))
        item = self.free_tracks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "???????????????????????????????? (??.)"))
        item = self.free_tracks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "???????????????? ????????"))
        self.a_way.setText(_translate("MainWindow", "?????????????????? ?? ????????"))
        item = self.a_way_trucks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????????????????"))
        item = self.a_way_trucks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????????????"))
        item = self.a_way_trucks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "?????? ???????????? (??.)"))
        item = self.a_way_trucks.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "????????"))
        item = self.a_way_trucks.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "???????????????? (??.)"))
        self.control_trans_btn.setText(_translate("MainWindow", "???????????????????? ??????????????????????"))
        self.Table.setTabText(self.Table.indexOf(self.orders), _translate("MainWindow", "????????????"))
        self.control_btn.setText(_translate("MainWindow", "???????????????????? ?????????? ????????????????"))
        self.rating.setText(_translate("MainWindow", "?????????????? ???? ???????????????????? ???????????????????? ??????????????"))
        item = self.rating_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????????????"))
        item = self.rating_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????????????????"))
        self.story.setText(_translate("MainWindow", "?????????????? ?????????????? (???????????????? ??????????????)"))
        item = self.story_orders.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????????????????"))
        item = self.story_orders.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "??????????"))
        item = self.story_orders.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "????????"))
        item = self.story_orders.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "?????? (??.)"))
        self.Table.setTabText(self.Table.indexOf(self.clients), _translate("MainWindow", "??????????????"))
