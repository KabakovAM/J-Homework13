import interface
from calculation import calculation
from compl import compl
# Контролер всей программы

def button_click():
    typ = interface.main_menu()
    if typ == 0:
        return
    if typ == 1:
        op = interface.menu_1()
        if op == 0:
            return button_click()
        if op == 1:
            num = calculation('+')
        if op == 2:
            num = calculation('-')
        if op == 3:
            num = calculation('*')
        if op == 4:
            num = calculation('/')
    if typ == 2:
        op = interface.menu_2()
        if op == 0:
            return button_click()
        if op == 1:
            num = compl('+')
        if op == 2:
            num = compl('-')
        if op == 3:
            num = compl('*')
        if op == 4:
            num = compl('/')
    num.result()
    interface.end_programm()
