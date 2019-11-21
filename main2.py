import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint as r


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.p = QPushButton(self)
        self.p.move(200, 200)
        self.p.resize(150, 50)
        self.p.clicked.connect(self.drawFlag)
        self.setWindowTitle('Рисование')
        self.show()

    def drawFlag(self, qp):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(r(0, 255), r(0, 255), r(0, 255)))
        size = r(0, 400)
        qp.drawEllipse(r(0, 100), r(0, 100), size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
