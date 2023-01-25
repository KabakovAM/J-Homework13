from model_calculation import model_calculation
from data import data
from actions.sum import sum
from actions.sub import sub
from actions.mult import mult
from actions.div import div
import log


class calculation(model_calculation): #Основной класс, который реализует калькулятор (действительные числа).
    def __init__(self, op):
        self.op = op

    def result(self):
        a = data('\nВведите первое число: ')
        b = data('\nВведите второе число: ')
        if self.op == '+':
            result = sum(a.get_value(), b.get_value())
        if self.op == '-':
            result = sub(a.get_value(), b.get_value())
        if self.op == '*':
            result = mult(a.get_value(), b.get_value())
        if self.op == '/':
            result = div(a.get_value(), b.get_value())
        print(f'\n{result.get_a()} {self.op} {result.get_b()} = {result.result()}')
        log.operation_log(result.get_a(), self.op,
                             result.get_b(), result.result())
