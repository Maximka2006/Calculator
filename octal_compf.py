import re
from compf import Compf


class OctalCompf(Compf):
    SYMBOLS = re.compile(r"\d+|[-+*/()]")

    def __init__(self, right_assoc=[]):
        super().__init__(right_assoc)

    def compile(self, str):
        """Компилирует выражение в постфиксную запись с восьмеричными числами"""
        self.data.clear()
        tokens = self.tokenize("(" + str + ")")
        for token in tokens:
            self.process_symbol(token)
        return " ".join(self.data)

    def tokenize(self, formula):
        """Разбивает формулу на токены: числа и операторы"""
        tokens = []
        formula = formula.replace(' ', '')
        i = 0
        while i < len(formula):
            if formula[i].isdigit():
                j = i
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                tokens.append(formula[i:j])
                i = j
            elif formula[i] in '+-*/()':
                tokens.append(formula[i])
                i += 1
            else:
                raise ValueError(f"Invalid character: {formula[i]}")
        return tokens

    def check_symbol(self, c):
        """Проверяет допустимость символа"""
        if not c.isdigit():
            raise ValueError(f"Недопустимый символ '{c}'")
        num = int(c)
        if num < 1 or num > 3999:
            raise ValueError(f"Число {num} вне диапазона 1-3999")

    def process_value(self, c):
        """Преобразует число в восьмеричное и добавляет в выход"""
        octal = oct(int(c)).replace("0o", "0O", 1)
        self.data.append(octal)