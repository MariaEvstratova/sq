import sqlite3

from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import sqlite3


class Results(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM coffee").fetchall()
        for i in range(0, len(result)):
            ii = result[i]
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(str(ii[0])))
            self.table.setItem(i, 1, QTableWidgetItem(ii[1]))
            self.table.setItem(i, 2, QTableWidgetItem(ii[2]))
            self.table.setItem(i, 3, QTableWidgetItem(ii[3]))
            self.table.setItem(i, 4, QTableWidgetItem(ii[4]))
            self.table.setItem(i, 5, QTableWidgetItem(ii[5]))
            self.table.setItem(i, 6, QTableWidgetItem(ii[6]))
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Results()
    ex.show()
    sys.exit(app.exec())