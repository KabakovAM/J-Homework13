import exception
import controller

# Пользовательский интерфейс
def main_menu():
    print('\nКалькулятор!')
    print('\nВыберите тип числа:\n1 - Действительное\n2 - Комплексное\n0 - Выйти из программы')
    data = input()
    if exception.type_op(data, 2):
        return int(data)
    print('\nОшибка ввода!')
    return main_menu()


def menu_1():
    print('\nДействительные числа:')
    print('\nВыберите действие:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n0 - Выйти в предыдущее меню')
    data = input()
    if exception.type_op(data, 4):
        return int(data)
    print('\nОшибка ввода!')
    return menu_1()


def menu_2():
    print('\nКомплексные числа:')
    print('\nВыберите действие:\n1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n0 - Выйти в предыдущее меню')
    data = input()
    if exception.type_op(data, 4):
        return int(data)
    print('\nОшибка ввода!')
    return menu_1()


def end_programm():
    print('\nВыберите опцию: ')
    print('\nПродолжить работу с калькулятором?\n1 - Да\n0 - Нет')
    data = input()
    if exception.type_op(data, 1):
        if int(data) == 1:
            return controller.button_click()
        if int(data) == 0:
            return
    print('\nОшибка ввода!')
    return end_programm()
