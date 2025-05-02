# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication, QTime, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent 
from PyQt5.QtGui import * 
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets, QtCore
import sys
from os import path

#import UI file
FORM_CLASS,_ =loadUiType(path.join(path.dirname(__file__),'calculatrice.ui'))	

class Resto(QMainWindow, FORM_CLASS):
    invoice_no = 0
    def __init__(self, parent=None):
        super(Resto, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.maFenetre()

        # grid = QGridLayout()             # l, c, h, w
        screen = QLCDNumber()
        self.grid.addWidget(screen, 0, 0, 1, 4)

        self.grid.addWidget(QPushButton("MC"), 1, 0)
        self.grid.addWidget(QPushButton("M+"), 1, 1)
        self.grid.addWidget(QPushButton("/"), 1, 2)
        self.grid.addWidget(QPushButton("*"), 1, 3)

        self.grid.addWidget(QPushButton("7"), 2, 0)
        self.grid.addWidget(QPushButton("8"), 2, 1)
        self.grid.addWidget(QPushButton("9"), 2, 2)
        self.grid.addWidget(QPushButton("-"), 2, 3)

        self.grid.addWidget(QPushButton("4"), 3, 0)
        self.grid.addWidget(QPushButton("5"), 3, 1)
        self.grid.addWidget(QPushButton("6"), 3, 2)
        self.grid.addWidget(QPushButton("+"), 3, 3)

        one_button = QPushButton("1")
        # one_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(one_button, 4, 0)
        two_button = QPushButton("2")
        # two_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(two_button, 4, 1)
        three_button = QPushButton("3")
        # three_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(three_button, 4, 2)
        equal_button = QPushButton("=")
        # equal_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(equal_button, 4, 3, 2, 1)

        self.grid.addWidget(QPushButton("0"), 5, 0, 1, 2)
        self.grid.addWidget(QPushButton("."), 5, 2)

        for line in range(6):
            self.grid.setRowStretch(line, 2 if line == 0 else 1)

        for idx in range(self.grid.count()):
            item: QLayoutItem = self.grid.itemAt(idx)
            widget = item.widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if isinstance(widget, QPushButton):
                widget.setStyleSheet("background: #595959; color: white; font-weight: bold; font-size: 20px")
            else:
                widget.setStyleSheet("background: #a2af77; font-weight: bold")

        equal_button.setStyleSheet("background: #f05a2D; font-weight: bold; font-size: 20px; color: white;")
        # equal_button.setObjectName("equal")

		
    
    def maFenetre(self):            
        self.setFixedSize(520,500)
        # self.setWindowIcon(QIcon('chat.png'))     

# Execute app
def main():            
    app = QApplication(sys.argv)
    window = Resto()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
        
		
		
		
# import sys

# from PySide6.QtGui import QIcon
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLCDNumber, QSizePolicy, \
    # QLayoutItem, QLabel


# class MyWindow(QMainWindow):

    # def __init__(self):
        # super().__init__()
        # self.setWindowTitle("Super Calculator V0.1")
        # self.setWindowIcon(QIcon("icons/yes.png"))
        # self.resize(500, 500)
        # self.setStyleSheet("background: #333333; border: 10px solid #333333;")

        # central_widget = QWidget()      # La classe de base de tous composants graphiques (c'est un conteneur)
        # self.setCentralWidget(central_widget)

        # grid = QGridLayout()             # l, c, h, w
        # screen = QLCDNumber()
        # grid.addWidget(screen, 0, 0, 1, 4)

        # grid.addWidget(QPushButton("MC"), 1, 0)
        # grid.addWidget(QPushButton("M+"), 1, 1)
        # grid.addWidget(QPushButton("/"), 1, 2)
        # grid.addWidget(QPushButton("*"), 1, 3)

        # grid.addWidget(QPushButton("7"), 2, 0)
        # grid.addWidget(QPushButton("8"), 2, 1)
        # grid.addWidget(QPushButton("9"), 2, 2)
        # grid.addWidget(QPushButton("-"), 2, 3)

        # grid.addWidget(QPushButton("4"), 3, 0)
        # grid.addWidget(QPushButton("5"), 3, 1)
        # grid.addWidget(QPushButton("6"), 3, 2)
        # grid.addWidget(QPushButton("+"), 3, 3)

        # one_button = QPushButton("1")
        # # one_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # grid.addWidget(one_button, 4, 0)
        # two_button = QPushButton("2")
        # # two_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # grid.addWidget(two_button, 4, 1)
        # three_button = QPushButton("3")
        # # three_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # grid.addWidget(three_button, 4, 2)
        # equal_button = QPushButton("=")
        # # equal_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # grid.addWidget(equal_button, 4, 3, 2, 1)

        # grid.addWidget(QPushButton("0"), 5, 0, 1, 2)
        # grid.addWidget(QPushButton("."), 5, 2)

        # for line in range(6):
            # grid.setRowStretch(line, 2 if line == 0 else 1)

        # for idx in range(grid.count()):
            # item: QLayoutItem = grid.itemAt(idx)
            # widget = item.widget()
            # widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # if isinstance(widget, QPushButton):
                # widget.setStyleSheet("background: #595959; color: white; font-weight: bold; font-size: 20px")
            # else:
                # widget.setStyleSheet("background: #a2af77; font-weight: bold")

        # equal_button.setStyleSheet("background: #f05a2D; font-weight: bold; font-size: 20px; color: white;")
        # # equal_button.setObjectName("equal")

        # central_widget.setLayout(grid)


# if __name__ == "__main__":
    # app = QApplication(sys.argv)

    # myWindow = MyWindow()
    # myWindow.show()

    # sys.exit(app.exec())

