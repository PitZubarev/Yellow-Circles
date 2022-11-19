from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPolygon, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint, choice
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 300, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Click for circle"))


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.colors = [
            'Red', 'Orange', 'Yellow', 'Green', 'Cyan',
            'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
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
            qp.setBrush(QColor(choice(self.colors)))
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