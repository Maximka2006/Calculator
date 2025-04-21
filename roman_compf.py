import re
from compf import Compf


class RomanCompf(Compf):
    SYMBOLS = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

    def __init__(self):
        super().__init__()

    def compile(self, str):
        self.data.clear()
        tokens = self.tokenize("(" + str + ")")
        for token in tokens:
            self.process_symbol(token)
        return " ".join(self.data).lower()

    def tokenize(self, formula):
        tokens = []
        formula = formula.replace(' ', '')
        i = 0
        while i < len(formula):
            if formula[i] in "IVXLCDM":
                j = i
                while j < len(formula) and formula[j] in "IVXLCDM":
                    j += 1
                tokens.append(formula[i:j])
                i = j
            elif formula[i] in '+-*/()':
                tokens.append(formula[i])
                i += 1
            else:
                raise ValueError(f"Недопустимый символ: {formula[i]}")
        return tokens

    def check_symbol(self, c):
        if c in '+-*/()':
            return
        if not self.is_roman(c):
            raise ValueError(f"Некорректное римское число: {c}")
        if not self.SYMBOLS.match(c):
            raise ValueError(f"Недопустимая комбинация символов: {c}")

    @staticmethod
    def is_roman(s):
        roman_numerals = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        return all(ch in roman_numerals for ch in s)

    @staticmethod
    def roman_to_int(s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for c in s[::-1]:
            current = roman[c]
            if current < prev:
                total -= current
            else:
                total += current
            prev = current
        return total

    def process_value(self, c):
        num = self.roman_to_int(c)
        if num > 3999:
            raise ValueError(f"Число {num} превышает максимальное допустимое (3999)")
        hex_num = hex(num).upper().replace("0X", "0x", 1)
        self.data.append(hex_num)

    @staticmethod
    def priority(c):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(c, 0)

    @staticmethod
    def is_precedes(a, b):
        if a == "(":
            return False
        elif b == ")":
            return True
        else:
            return RomanCompf.priority(a) >= RomanCompf.priority(b)