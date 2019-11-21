import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.update_result)
        self.setWindowTitle('Телефонный справочник')

    def update_result(self):
        cur = self.con.cursor()
        self.tableWidget.setHorizontalHeaderLabels(['Id', 'Сорт', 'Степень обжарки', 'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки'])
        rr = """SELECT * FROM coffes"""
        result = cur.execute(rr).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            self.dictionary[self.titles[1]].append(elem)
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())