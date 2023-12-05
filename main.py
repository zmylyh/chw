import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import GUI
import algorithm as algo
import source

stop_list = []  # list of stops: [[line, station], ...]
result_list = []  # list of the result [str, str, ...]
result_route = ''
total_time = 0


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
    # create two temp widgets
    cb_line = QtWidgets.QComboBox()
    add_item_cb(cb_line, ['', '1', '2', '3'])
    cb_station = QtWidgets.QComboBox()

    def add_tmp():
        add_by_line(cb_station, cb_line.currentText())

    # create connection between the column 1 and column 2
    cb_line.currentIndexChanged.connect(add_tmp)
    table = UI.stopover_list
    if table.columnCount() == 0:
        # only add column headers when the table is empty
        add_multi_column(['line', 'station'], table)
    add_multi_row([str(table.rowCount() + 1)], table)
    # add into the table
    table.setCellWidget(table.rowCount() - 1, 0, cb_line)
    table.setCellWidget(table.rowCount() - 1, 1, cb_station)
    # set the cell width to increase readability
    UI.stopover_list.setColumnWidth(1, 200)


def del_stopover():
    table = UI.stopover_list
    table.removeRow(table.rowCount() - 1)
    if table.rowCount() == 0:
        table.setColumnCount(0)


def remove_blank():
    # remove blank lines if the user leave some
    table = UI.stopover_list
    for i in range(table.rowCount() - 1, -1, -1):
        if table.cellWidget(i, 0).currentIndex() == 0:
            table.removeRow(i)
    # remove the header if there is no stopover left
    if table.rowCount() == 0:
        table.setColumnCount(0)


def is_transfer(station: str):
    return station in source.transfer_list


def get_stop_list():
    global stop_list
    stop_list.clear()
    stop = [UI.start_line.currentText(), UI.start_station.currentText()]
    stop_list.append(stop.copy())
    table = UI.stopover_list
    if table.rowCount() > 0:
        # get the stopovers in the table
        for r in range(table.rowCount()):
            stop.clear()
            stop.append(table.cellWidget(r, 0).currentText())
            stop.append(table.cellWidget(r, 1).currentText())
            stop_list.append(stop.copy())
    stop.clear()
    stop = [UI.end_line.currentText(), UI.end_station.currentText()]
    stop_list.append(stop)


def calculate_all():
    global stop_list
    global result_list
    global total_time
    result_list.clear()
    total_time = 0
    prf = UI.preference.currentIndex()
    for i in range(len(stop_list) - 1):
        start = stop_list[i][1]
        end = stop_list[i + 1][1]
        if prf == 1:
            # when the preference is 'minimize transfer', check if the station is in the transfer_list
            if is_transfer(start):
                start += stop_list[i][0]
            if is_transfer(end):
                end += stop_list[i + 1][0]
            result = algo.dijkstra(source.graph2, start, end)

        else:
            # the preference is 'shortest time'
            result = algo.dijkstra(source.graph, start, end)

        if type(result) == str:
            # no possible route
            result_list.clear()
            result_list.append(result)
        else:
            result_list.append(result[0])
            total_time += result[1]
    return result_list


def show_result():
    global total_time
    show_str = ''
    UI.result.setText('')
    if "Route Not Possible" in result_list:
        show_str = result_list[0]
    else:
        for i in range(len(result_list)):
            show_str += f'{stop_list[i][1]} to {stop_list[i + 1][1]}:\n'
            show_str += f'{result_list[i]}\n\n'
        show_str += f'Total time: {total_time}'
    UI.result.setText(show_str)


def clear_inputs():
    UI.start_line.setCurrentIndex(0)
    UI.start_station.clear()
    UI.end_line.setCurrentIndex(0)
    UI.end_station.clear()
    UI.stopover_list.clear()
    UI.stopover_list.setRowCount(0)
    UI.stopover_list.setColumnCount(0)
    UI.preference.setCurrentIndex(0)


def calculate_route_slot():
    if UI.start_line.currentIndex() == 0 or UI.end_line.currentIndex() == 0:
        return
    remove_blank()
    get_stop_list()
    calculate_all()
    show_result()
    # clear_inputs()
    UI.stack.setCurrentIndex(1)


def setup_map():
    UI.map_line.setCurrentIndex(0)
    scene.clear()
    UI.stack.setCurrentIndex(2)


def show_map():
    img = QtGui.QPixmap()
    if UI.map_line.currentText() == '':
        # if the user select nothing, clear the viewer
        scene.clear()
        return
    # load the map picture
    img.load(f'img/line{UI.map_line.currentText()}.png')
    img_item = QtWidgets.QGraphicsPixmapItem()
    img_item.setPixmap(QtGui.QPixmap(img))
    scene.clear()
    scene.addItem(img_item)


if __name__ == '__main__':
    # program setup
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI.Ui_MainWindow()
    UI.setupUi(Main)
    Main.setWindowTitle('SRP System')

    # initialise widgets
    add_item_cb(UI.start_line, ['', '1', '2', '3'])
    add_item_cb(UI.end_line, ['', '1', '2', '3'])
    add_item_cb(UI.map_line, ['', '总线', '1', '2', '3', '3(北延段)'])
    add_item_cb(UI.preference, ['shortest time', 'minimize transfers'])
    UI.preference.setCurrentIndex(0)

    # graphicView setup
    scene = QtWidgets.QGraphicsScene()
    UI.map_view.setScene(scene)

    # connections
    UI.start_line.currentIndexChanged.connect(show_start_list)
    UI.end_line.currentIndexChanged.connect(show_end_list)
    UI.add_button.clicked.connect(add_stopover)
    UI.delete_button.clicked.connect(del_stopover)
    UI.calculate.clicked.connect(calculate_route_slot)
    UI.return_home.clicked.connect(lambda turn: UI.stack.setCurrentIndex(0))
    UI.return_home_2.clicked.connect(lambda turn: UI.stack.setCurrentIndex(0))
    UI.map_line.currentIndexChanged.connect(show_map)
    UI.show_map.clicked.connect(setup_map)

    UI.stack.setCurrentIndex(0)
    Main.show()
    UI.map_view.show()

    # close condition
    sys.exit(app.exec())
