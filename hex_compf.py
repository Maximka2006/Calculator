
import re
from compf import Compf


class HexCompf(Compf):
    SYMBOLS = re.compile(r"0[xX][0-9A-Fa-f]+|[-+*/()]")

    def __init__(self):
        super().__init__()

    def compile(self, str):
        if not str.strip():
            raise ValueError("Пустая строка недопустима")
        self.data.clear()
        tokens = self.tokenize("(" + str + ")")
        for token in tokens:
            self.process_symbol(token)
        return " ".join(self.data)

    def tokenize(self, formula):
        tokens = []
        formula = formula.replace(' ', '')
        i = 0
        while i < len(formula):
            if formula[i] == '0' and i+1 < len(formula) and formula[i+1].lower() == 'x':
                j = i + 2
                while j < len(formula) and formula[j].lower() in "0123456789abcdef":
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
        if not self.SYMBOLS.match(c):
            raise ValueError(f"Недопустимый символ '{c}'")
 
    def process_value(self, c):
        num = int(c, 16)
        if num > 3999:
            raise ValueError(f"Число {num} превышает 3999")
        self.data.append(c.lower())

    @staticmethod
    def priority(c):
        return 1 if c in '+-' else 2  # +- имеют приоритет 1, */ - приоритет 2

    @staticmethod
    def is_precedes(a, b):
        if a == "(":
            return False
        elif b == ")":
            return True
        else:
            return HexCompf.priority(a) >= HexCompf.priority(b)