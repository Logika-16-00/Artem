
from PyQt5.QtWidgets import QLineEdit, QPushButton,QFormLayout,QListWidget,QVBoxLayout,QWidget,QHBoxLayout

line_ans = QLineEdit('')
line_correct = QLineEdit('')
line_false1 = QLineEdit('')
line_false2 = QLineEdit('')
line_false3 = QLineEdit('')

form = QFormLayout()
form.addRow('Введіть запитання', line_ans)
form.addRow('Введіть правельну відповідь', line_correct)

form.addRow('Введіть неправильний варіант1', line_false1)

form.addRow('Введіть неправильний варіант2', line_false2)

form.addRow('Введіть неправильний варіант3', line_false3)
line_q = QListWidget()
                                                                 
btn_add = QPushButton('додати запитання')
btn_clear = QPushButton('очистити')
btn_back = QPushButton('назад')

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)

line1 = QVBoxLayout()
line1.addWidget(line_q,stretch= 3)
line1.addWidget(btn_add)

line2 = QVBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(btn_clear)
line3 = QVBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)

line4 = QVBoxLayout()
line3.addWidget(btn_back,stretch=2)
main_menu_line = QHBoxLayout()
main_menu_line.addLayout(line3)
main_menu_line.addLayout(line4)





































