from model import model


class sum(model): #Класс сложения чисел
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def result(self):
        return (self.a + self.b)

    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
