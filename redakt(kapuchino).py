import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hohly.ui', self)
        self.con = sqlite3.connect("films.db")
        self.update_result()
        self.setWindowTitle('Телефонный справочник')
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton.clicked.connect()
        self.pushButton_2.clicked.connect(self.save_results)
        self.modified = {}
        self.titles = None
        self.dictionary = {}

    def update_result(self):
        cur = self.con.cursor()
        self.tableWidget.setHorizontalHeaderLabels(
            ['Id', 'Сорт', 'Степень обжарки', 'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки'])
        rr = """SELECT * FROM coffes"""
        result = cur.execute(rr).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.dictionary['title'] = []
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            self.dictionary[self.titles[1]].append(elem)
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()
        self.number = item.row()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE coffes SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE title="
            cur.execute(que + '\'' + self.dictionary['title'][self.number][1] + '\'')
            self.con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())