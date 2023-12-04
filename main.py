import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import GUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI.Ui_MainWindow()
    UI.setupUi(Main)


    UI.stack.setCurrentIndex(0)
    Main.show()
    sys.exit(app.exec())