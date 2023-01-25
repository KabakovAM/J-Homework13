from model_calculation import model_calculation
from data import data
from actions.sum import sum
from actions.sub import sub
from actions.mult import mult
from actions.div import div
import log


class compl(model_calculation): #Основной класс, который реализует калькулятор (комплексные числа).
    def __init__(self, op):
        self.op = op

    def result(self):
        a = data('\nВведите вещественную часть первого числа: ')
        b = data('\nВведите мнимую часть первого числа: ')
        c = data('\nВведите вещественную часть второго числа: ')
        d = data('\nВведите мнимую часть второго числа: ')
        if self.op == '+':
            result = sum(complex(a.get_value(), b.get_value()),
                         complex(c.get_value(), d.get_value()))
        if self.op == '-':
            result = sub(complex(a.get_value(), b.get_value()),
                         complex(c.get_value(), d.get_value()))
        if self.op == '*':
            result = mult(complex(a.get_value(), b.get_value()),
                          complex(c.get_value(), d.get_value()))
        if self.op == '/':
            result = div(complex(a.get_value(), b.get_value()),
                         complex(c.get_value(), d.get_value()))
        print(f'\n{result.get_a()} {self.op} {result.get_b()} = {result.result()}')
        log.operation_log(result.get_a(), self.op,
                          result.get_b(), result.result())
