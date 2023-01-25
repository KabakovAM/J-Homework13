from abc import ABC, abstractclassmethod


class model_calculation(ABC): #Абстрактный класс который реализует калькулятор
    @abstractclassmethod
    def result():
        pass
