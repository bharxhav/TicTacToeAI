from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("tic-tac-toe.ui", self)
        self.position = {i: None for i in range(1, 10)}
        self.counter = 0

        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.label = self.findChild(QLabel, "label")

        self.buttons = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9]

        self.button1.clicked.connect(lambda: self.clicker(self.button1, 1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2, 2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3, 3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4, 4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5, 5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6, 6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7, 7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8, 8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9, 9))
        self.button10.clicked.connect(self.reset)

        self.show()

    def checkWin(self):
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1, self.button4, self.button7)

        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8)

        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3)

        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6)

        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9)

        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7)

    def win(self, a, b, c):
        a.setStyleSheet('QPushButton {color: red;}')
        b.setStyleSheet('QPushButton {color: red;}')
        c.setStyleSheet('QPushButton {color: red;}')

        self.label.setText(f"{a.text()} Wins!")

        self.disable()

    def disable(self):
        for b in self.buttons:
            b.setEnabled(False)

    def clicker(self, b, pos):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)
        self.position[pos] = 1 if mark == "X" else 0

        self.counter += 1
        self.checkWin()

    def reset(self):
        self.position = {i: None for i in range(1, 10)}
        for b in self.buttons:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet('QPushButton {color: #797979;}')

        self.label.setText("You Go First!")
        self.counter = 0


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
