from PyQt5.QtWidgets import QWidget
from card import *
from menu import *
from data import *

radio_list = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]
frm_card = 0 
form_list =[]
# Тестові данні
def testlist():

    frm = Question('Максимальна висота атмосфери', '11000м', '1100м', '5000м', '25000м')
    form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    form_list.append(frm)
    frm = Question('Найпопулярніша гра в світі', 'Minecraft', 'GTA V', 'Roblox', 'Cs:Go')
    form_list.append(frm)
from app import App 
win_card = QWidget()
win_menu = QWidget()
def set_card():
    win_card.resize(600,500)
    win_card.setWindowTitle("Memory menu")
    win_card.move(0,0)
    win_card.setLayout(mani_line)
def set_menu():
    win_menu.resize(800,800)
    win_menu.setWindowTitle("Memory Card")
    win_menu.move(0,0) 
    win_menu.setLayout(main_menu_line)
  
def back_to_menu():
    win_card.hide()
    win_menu.show()    

def back_to_test():
    win_menu.hide()
    win_card.show()
btn_back.clicked.connect(back_to_test)    
btn_menu.clicked.connect(back_to_menu)
def show_q():
    list_q.clear()
    for q in form_list:
        list_q.addItem(q.name)
testlist()
show_q()

def clear():
    line_ans.clear()
    line_correct.clear()
    line_false1.clear()
    line_false2.clear()
    line_false3.clear()
btn_clear.clicked.connect(clear)  

set_card()
set_menu()
win_card.show()
App.exec_()

win_card = QWidget()


win_card.setLayout(mani_line)

win_card.show()
App.exec_()






