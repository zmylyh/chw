import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import GUI
import graph
import source


def add_item_cb(cb: QtWidgets.QComboBox, data_list: list):
    for item in data_list:
        cb.addItem(item)

def add_by_line(cb: QtWidgets.QComboBox, line: str):
    cb.clear()
    if line == '1':
        add_item_cb(cb, source.l1)
    elif line == '2':
        add_item_cb(cb, source.l2)
    elif line == '3':
        add_item_cb(cb, source.l3)

def show_start_list():
    line = UI.start_line.currentText()
    dest = UI.start_station
    add_by_line(dest, line)

def show_end_list():
    line = UI.end_line.currentText()
    dest = UI.end_station
    add_by_line(dest, line)






def add_column(col: int, header: str, table):
    table.insertColumn(col)
    table.setHorizontalHeaderItem(col, QtWidgets.QTableWidgetItem(header))


def add_multi_column(header_list: list | tuple, table):
    for i in range(len(header_list)):
        add_column(table.columnCount(), header_list[i], table)


def add_row(row: int, header: str, table):
    table.insertRow(row)
    table.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(header))


def add_multi_row(header_list: list | tuple, table):
    for i in range(len(header_list)):
        add_row(table.rowCount(), header_list[i], table)


def add_stopover():
    cb_line = QtWidgets.QComboBox()
    add_item_cb(cb_line, ['', '1', '2', '3'])
    cb_station = QtWidgets.QComboBox()

    def add_tmp():
        add_by_line(cb_station, cb_line.currentText())
    cb_line.currentIndexChanged.connect(add_tmp)

    table = UI.stopover_list
    if table.columnCount() == 0:
        add_multi_column(['line', 'station'], table)
    add_multi_row([str(table.rowCount() + 1)], table)
    table.setCellWidget(table.rowCount() - 1, 0, cb_line)
    table.setCellWidget(table.rowCount() - 1, 1, cb_station)
    UI.stopover_list.setColumnWidth(1, 200)


def del_stopover():
    table = UI.stopover_list
    table.removeRow(table.rowCount() - 1)
    if table.rowCount() == 0:
        table.setColumnCount(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI.Ui_MainWindow()
    UI.setupUi(Main)

    add_item_cb(UI.start_line, ['', '1', '2', '3'])
    add_item_cb(UI.end_line, ['', '1', '2', '3'])



    UI.start_line.currentIndexChanged.connect(show_start_list)
    UI.end_line.currentIndexChanged.connect(show_end_list)
    UI.add_button.clicked.connect(add_stopover)
    UI.delete_button.clicked.connect(del_stopover)


    UI.stack.setCurrentIndex(0)
    Main.show()
    sys.exit(app.exec())