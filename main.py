from mod_func_centroides import *
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QAbstractTableModel, Qt


class PandasModel(QAbstractTableModel):

    def __init__(self, datos):
        QAbstractTableModel.__init__(self)
        self._datos = datos

    def rowCount(self, parent=None):
        return self._datos.shape[0]

    def columnCount(self, parent=None):
        return self._datos.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._datos.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._datos.columns[col]
        return None


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Cargando la config del uic
        uic.loadUi("centroidesMainWindow.ui", self)


def main():
    app = QApplication(sys.argv)
    mainWindow = VentanaPrincipal()
    mainWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
