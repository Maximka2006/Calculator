
import re
from operator import add, sub, mul, truediv
from stack import Stack
from hex_compf import HexCompf


class HexCalc(HexCompf):
    def __init__(self):
        super().__init__()
        self.r = Stack()

    def compile(self, str):
        super().compile(str)
        return self.r.top()

    def process_value(self, c):
        num = int(c, 16)
        if num > 3999:
            raise ValueError(f"Число {num} превышает 3999")
        self.r.push(num)

    def process_oper(self, c):
        second, first = self.r.pop(), self.r.pop()
        self.r.push({"+": add, "-": sub, "*": mul, "/": truediv}[c](first, second))