
import re
from stack import Stack


class Compf:


    SYMBOLS = re.compile("[a-z]")

    def __init__(self, right_assoc=[]):
        self.right_assoc = right_assoc
        self.s = Stack()
        # результат компиляции
        self.data = []

    def compile(self, str):
        self.data.clear()
        # Последовательный вызов для всех символов
        for c in "(" + str + ")":
            self.process_symbol(c)
        return " ".join(self.data)

    # Обработка символа
    def process_symbol(self, c):
        if c == "(":
            self.s.push(c)
        elif c == ")":
            self.process_suspended_operators(c)
            self.s.pop()
        elif c in "+-*/":
            self.process_suspended_operators(c)
            self.s.push(c)
        else:
            self.check_symbol(c)
            self.process_value(c)

    # Обработка отложенных операций
    def process_suspended_operators(self, c):
        while self.is_precedes(self.s.top(), c):  
            self.process_oper(self.s.pop())

    # Обработка имени переменной
    def process_value(self, c):
        self.data.append(c)

    # Обработка символа операции
    def process_oper(self, c):
        self.data.append(c)

    # Проверка допустимости символа
    def check_symbol(self, c):
        if not self.SYMBOLS.match(c):
            raise Exception(f"Недопустимый символ '{c}'")

    # Определение приоритета операции
    def priority(c):
        return 1 if (c == "+" or c == "-") else 2

    def is_precedes(self, a, b):
        if a == "(":
            return False
        elif b == ")":
            return True
        elif (a==b) and (a in self.right_assoc):
            return False  # Правоассоциативность для операции для которой это задано
        else:
            return Compf.priority(a) >= Compf.priority(b)


if __name__ == "__main__":
    c = Compf()
    while True:
        str = input("Арифметическая  формула: ")
        print(f"Результат её компиляции: {c.compile(str)}")
        print()
