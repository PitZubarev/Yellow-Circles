from PyQt5.QtGui import QPolygon, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randint
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)
        self.initUi()
        self.tool = 0
    
    def initUi(self):
        self.pushButton.clicked.connect(self.run)
    
    def run(self):
        self.tool = 1
        self.update()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.tool == 1:
            qp.setBrush(QColor('Yellow'))
            radius = randint(1, 200)
            if radius % 2 == 1:
                radius += 1
            qp.drawEllipse(200 - radius // 2, 200 - radius // 2, radius, radius)
            self.tool = 0
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    exit(app.exec_())