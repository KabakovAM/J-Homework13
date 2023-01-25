import exception

class data(): # Класс который собирает информацию от пользователя
    def __init__(self, title):
        self.title = title

    def get_value(self):
        print(self.title)
        a = input()
        if not exception.number(a):
            print('\nВведено неверное значение! Повторите ввод!')
            return data.get_value(self)
        return int(a)

