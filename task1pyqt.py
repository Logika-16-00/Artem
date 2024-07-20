from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
def click():
    num_win = randint(0,100)
    txt1.setText('переможець')
    txt2.setText(str(num_win))

app = QApplication([])
win1 = QWidget()
win1.resize(1500,1500)
win1.move(0,0)
win1.setWindowTitle('ararararararararararrararaarararrararrrararararararar')
txt1 = QLabel('Нажми на кнопку(не знаю для чого)')
txt2 = QLabel('?')
bnt = QPushButton('нажми')
bnt.clicked.connect(click)
line = QVBoxLayout()
line.addWidget(txt1, alignment=Qt.AlignCenter)
line.addWidget(txt2)
line.addWidget(bnt)
win1.setLayout(line)
win1.show()

win1.show()
app.exec_()
