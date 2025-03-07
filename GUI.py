# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1266, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.upper = QtWidgets.QGridLayout()
        self.upper.setObjectName("upper")
        self.title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.upper.addWidget(self.title, 0, 0, 1, 1)
        self.subtitle = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle.setFont(font)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")
        self.upper.addWidget(self.subtitle, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.upper, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.frame)
        self.frame_15 = QtWidgets.QFrame(self.page)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_10 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_21.addWidget(self.label_10, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_21.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_21.addWidget(self.label_11, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_21.setColumnStretch(0, 5)
        self.gridLayout_21.setColumnStretch(1, 1)
        self.gridLayout_21.setColumnStretch(2, 6)
        self.gridLayout_21.setColumnStretch(3, 1)
        self.gridLayout_21.setColumnStretch(4, 5)
        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.frame_15)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.middle = QtWidgets.QHBoxLayout()
        self.middle.setObjectName("middle")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.mleft = QtWidgets.QGridLayout()
        self.mleft.setObjectName("mleft")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mleft.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mleft.addItem(spacerItem3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.mleft.addWidget(self.label_3, 3, 0, 1, 1)
        self.start_line = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_line.sizePolicy().hasHeightForWidth())
        self.start_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start_line.setFont(font)
        self.start_line.setObjectName("start_line")
        self.mleft.addWidget(self.start_line, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.mleft.addWidget(self.label_2, 1, 0, 1, 1)
        self.start_station = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_station.sizePolicy().hasHeightForWidth())
        self.start_station.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start_station.setFont(font)
        self.start_station.setObjectName("start_station")
        self.mleft.addWidget(self.start_station, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mleft.addItem(spacerItem4, 4, 1, 1, 1)
        self.mleft.setColumnStretch(0, 2)
        self.mleft.setColumnStretch(1, 3)
        self.mleft.setRowStretch(0, 1)
        self.mleft.setRowStretch(1, 2)
        self.mleft.setRowStretch(2, 1)
        self.mleft.setRowStretch(3, 2)
        self.mleft.setRowStretch(4, 1)
        self.gridLayout_7.addLayout(self.mleft, 0, 0, 1, 1)
        self.middle.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.arrow_1 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.arrow_1.setFont(font)
        self.arrow_1.setObjectName("arrow_1")
        self.gridLayout.addWidget(self.arrow_1, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.middle.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.mmiddle = QtWidgets.QGridLayout()
        self.mmiddle.setObjectName("mmiddle")
        self.delete_button = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("QPushButton{background-color: rgb(255, 30, 0); border-radius:10px; color:rgb(255,255,255);}")
        self.delete_button.setObjectName("delete_button")
        self.mmiddle.addWidget(self.delete_button, 2, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("QPushButton{background-color: rgb(0, 119, 237); border-radius:10px; color:rgb(255,255,255);}")
        self.add_button.setObjectName("add_button")
        self.mmiddle.addWidget(self.add_button, 0, 0, 1, 1)
        self.stopover_list = QtWidgets.QTableWidget(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stopover_list.setFont(font)
        self.stopover_list.setObjectName("stopover_list")
        self.stopover_list.setColumnCount(0)
        self.stopover_list.setRowCount(0)
        self.mmiddle.addWidget(self.stopover_list, 1, 0, 1, 1)
        self.mmiddle.setRowStretch(0, 1)
        self.mmiddle.setRowStretch(1, 5)
        self.mmiddle.setRowStretch(2, 1)
        self.gridLayout_9.addLayout(self.mmiddle, 0, 0, 1, 1)
        self.middle.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.arrow_2 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.arrow_2.setFont(font)
        self.arrow_2.setObjectName("arrow_2")
        self.verticalLayout.addWidget(self.arrow_2)
        self.gridLayout_12.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.middle.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.mright = QtWidgets.QGridLayout()
        self.mright.setObjectName("mright")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.mright.addWidget(self.label_4, 1, 0, 1, 1)
        self.end_line = QtWidgets.QComboBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_line.sizePolicy().hasHeightForWidth())
        self.end_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.end_line.setFont(font)
        self.end_line.setObjectName("end_line")
        self.mright.addWidget(self.end_line, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mright.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mright.addItem(spacerItem6, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.mright.addWidget(self.label_5, 3, 0, 1, 1)
        self.end_station = QtWidgets.QComboBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_station.sizePolicy().hasHeightForWidth())
        self.end_station.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.end_station.setFont(font)
        self.end_station.setObjectName("end_station")
        self.mright.addWidget(self.end_station, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mright.addItem(spacerItem7, 4, 1, 1, 1)
        self.mright.setColumnStretch(0, 2)
        self.mright.setColumnStretch(1, 3)
        self.mright.setRowStretch(0, 1)
        self.mright.setRowStretch(1, 2)
        self.mright.setRowStretch(2, 1)
        self.mright.setRowStretch(3, 2)
        self.mright.setRowStretch(4, 1)
        self.gridLayout_11.addLayout(self.mright, 0, 0, 1, 1)
        self.middle.addWidget(self.frame_5)
        self.middle.setStretch(0, 5)
        self.middle.setStretch(1, 1)
        self.middle.setStretch(2, 6)
        self.middle.setStretch(3, 1)
        self.middle.setStretch(4, 5)
        self.gridLayout_4.addLayout(self.middle, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 0, 2, 1, 1)
        self.preference = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preference.sizePolicy().hasHeightForWidth())
        self.preference.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.preference.setFont(font)
        self.preference.setObjectName("preference")
        self.gridLayout_6.addWidget(self.preference, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 2, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 1, 3, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 2)
        self.gridLayout_6.setColumnStretch(2, 2)
        self.gridLayout_6.setColumnStretch(3, 1)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 2)
        self.gridLayout_6.setRowStretch(2, 1)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.frame_3)
        self.frame_9 = QtWidgets.QFrame(self.page)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.show_map = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_map.sizePolicy().hasHeightForWidth())
        self.show_map.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.show_map.setFont(font)
        self.show_map.setStyleSheet("QPushButton{background-color: rgb(255,255,255); border-radius:20px; color:rgb(0, 119, 237);border-width:2px;border-color:rgb(0, 119, 237);border-style:outset;}")
        self.show_map.setObjectName("show_map")
        self.gridLayout_23.addWidget(self.show_map, 0, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem13, 0, 4, 1, 1)
        self.calculate = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculate.setFont(font)
        self.calculate.setStyleSheet("QPushButton{background-color: rgb(0, 119, 237); border-radius:20px; color:rgb(255,255,255);}")
        self.calculate.setObjectName("calculate")
        self.gridLayout_23.addWidget(self.calculate, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem14, 0, 2, 1, 1)
        self.gridLayout_23.setColumnStretch(0, 1)
        self.gridLayout_23.setColumnStretch(1, 2)
        self.gridLayout_23.setColumnStretch(2, 1)
        self.gridLayout_23.setColumnStretch(3, 2)
        self.gridLayout_23.setColumnStretch(4, 1)
        self.gridLayout_23.setRowStretch(0, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout_23)
        self.mainLayout.addWidget(self.frame_9)
        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 1)
        self.mainLayout.setStretch(2, 6)
        self.mainLayout.setStretch(3, 2)
        self.mainLayout.setStretch(4, 2)
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.frame_11 = QtWidgets.QFrame(self.page_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.result = QtWidgets.QTextBrowser(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.gridLayout_16.addWidget(self.result, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.page_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem15, 1, 0, 1, 1)
        self.return_home = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_home.sizePolicy().hasHeightForWidth())
        self.return_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_home.setFont(font)
        self.return_home.setStyleSheet("QPushButton{background-color: rgb(189,189,189); border-radius:20px; color:rgb(0,0,0);}")
        self.return_home.setObjectName("return_home")
        self.gridLayout_14.addWidget(self.return_home, 1, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem16, 1, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem17, 0, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem18, 2, 1, 1, 1)
        self.gridLayout_14.setColumnStretch(0, 2)
        self.gridLayout_14.setColumnStretch(1, 3)
        self.gridLayout_14.setColumnStretch(2, 2)
        self.gridLayout_14.setRowStretch(0, 1)
        self.gridLayout_14.setRowStretch(1, 5)
        self.gridLayout_14.setRowStretch(2, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stack.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.frame_13 = QtWidgets.QFrame(self.page_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.map_line = QtWidgets.QComboBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_line.sizePolicy().hasHeightForWidth())
        self.map_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.map_line.setFont(font)
        self.map_line.setObjectName("map_line")
        self.gridLayout_3.addWidget(self.map_line, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.page_3)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem19, 0, 0, 1, 1)
        self.map_view = QtWidgets.QGraphicsView(self.frame_14)
        self.map_view.setObjectName("map_view")
        self.gridLayout_19.addWidget(self.map_view, 0, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem20, 0, 2, 1, 1)
        self.gridLayout_19.setColumnStretch(0, 1)
        self.gridLayout_19.setColumnStretch(1, 5)
        self.gridLayout_19.setColumnStretch(2, 1)
        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_12 = QtWidgets.QFrame(self.page_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.return_home_2 = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_home_2.sizePolicy().hasHeightForWidth())
        self.return_home_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.return_home_2.setFont(font)
        self.return_home_2.setStyleSheet("QPushButton{background-color: rgb(189,189,189); border-radius:20px; color:rgb(0,0,0);}")
        self.return_home_2.setObjectName("return_home_2")
        self.gridLayout_10.addWidget(self.return_home_2, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem21, 0, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem22, 0, 2, 1, 1)
        self.gridLayout_10.setColumnStretch(0, 1)
        self.gridLayout_10.setColumnStretch(1, 2)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.gridLayout_18.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 6)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.stack.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stack)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.start_line, self.start_station)
        MainWindow.setTabOrder(self.start_station, self.add_button)
        MainWindow.setTabOrder(self.add_button, self.delete_button)
        MainWindow.setTabOrder(self.delete_button, self.end_line)
        MainWindow.setTabOrder(self.end_line, self.end_station)
        MainWindow.setTabOrder(self.end_station, self.preference)
        MainWindow.setTabOrder(self.preference, self.calculate)
        MainWindow.setTabOrder(self.calculate, self.result)
        MainWindow.setTabOrder(self.result, self.return_home)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Subway Route Planning System"))
        self.subtitle.setText(_translate("MainWindow", "Line 1-3 of Guangzhou Metro"))
        self.label_10.setText(_translate("MainWindow", "Stopover"))
        self.label_9.setText(_translate("MainWindow", "Start"))
        self.label_11.setText(_translate("MainWindow", "End"))
        self.label_3.setText(_translate("MainWindow", "Station"))
        self.label_2.setText(_translate("MainWindow", "Line"))
        self.arrow_1.setText(_translate("MainWindow", "→"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.arrow_2.setText(_translate("MainWindow", "→"))
        self.label_4.setText(_translate("MainWindow", "Line"))
        self.label_5.setText(_translate("MainWindow", "Station"))
        self.label.setText(_translate("MainWindow", "Preference"))
        self.show_map.setText(_translate("MainWindow", "Subway Map"))
        self.calculate.setText(_translate("MainWindow", "Calculate route"))
        self.label_6.setText(_translate("MainWindow", "Result"))
        self.return_home.setText(_translate("MainWindow", "Return"))
        self.label_7.setText(_translate("MainWindow", "Subway Map"))
        self.label_8.setText(_translate("MainWindow", "Select a line:"))
        self.return_home_2.setText(_translate("MainWindow", "Return"))
