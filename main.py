import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QTableWidgetItem
import sqlite3


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 120)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM coffee""").fetchall()
        index = 0
        self.tableWidget.setRowCount(len(result))
        for i in result:
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(i[0])))
            # for j in range(1, 4):
            t = cur.execute(f"""SELECT title FROM sorts_coffee WHERE id = {i[1]}""").fetchall()[0][0]
            self.tableWidget.setItem(index, 1, QTableWidgetItem(t))
            t = cur.execute(f"""SELECT title FROM stepen_obzharki WHERE id = {i[2]}""").fetchall()[0][0]
            self.tableWidget.setItem(index, 2, QTableWidgetItem(t))
            t = cur.execute(f"""SELECT title FROM type_coffee WHERE id = {i[3]}""").fetchall()[0][0]
            self.tableWidget.setItem(index, 3, QTableWidgetItem(t))
            for j in range(4, 7):
                self.tableWidget.setItem(index, j, QTableWidgetItem(str(i[j])))
            index += 1
        con.close()
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
