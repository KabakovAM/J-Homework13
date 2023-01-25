import datetime


def operation_log(num_1, op, num_2, result): # Логирование
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    with open('Homework13\log.txt', 'a', encoding='utf_8') as file:
        file.write(f'{time}; {num_1} {op} {num_2} = {result}\n')
