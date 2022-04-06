from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import random
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("tic-tac-toe.ui", self)
        self.position = {i: None for i in range(1, 10)}
        self.result = None
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

        self.lookup = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

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
        self.result = 1 if a.text() == "X" else -1
        self.disable()

    def disable(self):
        for b in self.buttons:
            b.setEnabled(False)

    def clicker(self, b, pos):
        me = False
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
            me = True
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)
        self.position[pos] = 1 if mark == "X" else 0

        self.counter += 1
        self.checkWin()

        if me and self.result is None:
            self.bestMove()

    def bestMove(self):
        possible = [
            key-1 for key in self.position if self.position[key] == None]

        if not possible:
            if not self.result:
                self.result = 0
            return

        state = self.makeState()

        ev = float('-inf')
        move = None

        for i in range(3):
            for j in range(3):
                if state[i][j] != -1:
                    continue

                state[i][j] = 1
                e = self.minimax(state, 9, False)
                state[i][j] = -1

                if e > ev:
                    ev = e
                    move = (i, j)

        print(move, ev)
        self.buttons[self.lookup[move[0]][move[1]]].click()

    def situation(self, state):
        for r in state:
            for ele in r:
                if ele == -1:
                    return None

        res = False
        if state[0][0] != -1:
            res = res or (state[0][0] == state[0][1] == state[0][2])
            res = res or (state[0][0] == state[1][1] == state[2][2])
            res = res or (state[0][0] == state[1][0] == state[2][0])

            if res:
                return -1 if state[0][0] == 0 else 1

        if state[0][2] != -1:
            res = res or (state[0][2] == state[1][1] == state[2][0])
            res = res or (state[0][2] == state[1][2] == state[2][2])

            if res:
                return -1 if state[0][2] == 0 else 1

        if state[1][1] != -1:
            res = res or (state[1][0] == state[1][1] == state[1][2])
            res = res or (state[0][1] == state[1][1] == state[2][1])

            if res:
                return -1 if state[1][1] == 0 else 1

        if state[2][0] != -1:
            res = res or (state[2][0] == state[2][1] == state[2][2])

            if res:
                return -1 if state[0][0] == 0 else 1

        return 0

    def getFenn(self, state):
        ret = ""

        for r in state:
            for ele in r:
                if ele == 1:
                    ret += 'X'
                elif ele == 0:
                    ret += 'O'
                else:
                    ret += 'N'

        return ret

    def evaluation(self, state):
        f = self.getFenn(state)
        x = o = 0

        if 'XX' in f:
            x += f.count('XX') * 2

        if 'OO' in f:
            o -= f.count('OO') * 2

        if f[0] == f[4] or f[4] == f[8]:
            if f[4] == 'X':
                x += 1
            else:
                o += 1

        if f[4] == f[6] or f[4] == f[2]:
            if f[4] == 'X':
                x += 1
            else:
                o += 1

        if f[0] == f[8]:
            if f[0] == 'X':
                x += 1
            else:
                o += 1

        if f[2] == f[6]:
            if f[2] == 'X':
                x += 1
            else:
                o += 1

        if f[0] == f[2]:
            if f[0] == 'X':
                x += 1
            else:
                o += 1

        if f[8] == f[6]:
            if f[6] == 'X':
                x += 1
            else:
                o += 1

        return x - o

    def makeState(self):
        state = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

        for key in self.position:
            sym = self.position[key]

            if sym is None:
                continue

            if 0 < key < 4:
                state[key-1][0] = sym
            elif 3 < key < 7:
                state[key-4][1] = sym
            else:
                state[key-7][2] = sym

        return state

    def minimax(self, state, depth, maxPlayer):
        sit = self.situation(state)

        if sit is not None:
            return sit * 10

        if depth == 0:
            return self.evaluation(state)

        ev = None

        if maxPlayer:
            ev = float('-inf')

            for i in range(3):
                for j in range(3):
                    if state[i][j] != -1:
                        continue

                    state[i][j] = 1
                    e = self.minimax(state, depth-1, False)
                    state[i][j] = -1

                    if e > ev:
                        ev = e
        else:
            ev = float('inf')

            for i in range(3):
                for j in range(3):
                    if state[i][j] != -1:
                        continue

                    state[i][j] = 0
                    e = self.minimax(state, depth-1, True)
                    state[i][j] = -1

                    if e < ev:
                        ev = e

        return ev

    def reset(self):
        for b in self.buttons:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet('QPushButton {color: #797979;}')

        self.position = {i: None for i in range(1, 10)}
        self.label.setText("You Go First!")
        self.counter = 0
        self.result = None


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
