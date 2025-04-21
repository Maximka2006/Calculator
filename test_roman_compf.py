import pytest
from roman_compf import RomanCompf


class TestRomanCompf:
    def setup_method(self):
        self.c = RomanCompf()

    def test_valid_roman_numbers(self):
        assert self.c.compile("IV") == "0x4"
        assert self.c.compile("MMMCMXCIX") == "0xf9f"
        assert self.c.compile("I + II") == "0x1 0x2 +"

    def test_invalid_roman_numbers(self):
        with pytest.raises(ValueError, match="Недопустимая комбинация символов"):
            self.c.compile("IIII")
        with pytest.raises(ValueError, match="Недопустимый символ"):
            self.c.compile("X + ABC")

    def test_operations(self):
        assert self.c.compile("X+V*II") == "0xa 0x5 0x2 * +"  
        assert self.c.compile("X-V/II") == "0xa 0x5 0x2 / -"

    def test_parentheses(self):
        assert self.c.compile("(X+V)*II") == "0xa 0x5 + 0x2 *"

if __name__ == "__main__":
    pytest.main(["-v", "/Users/maksim/Desktop/1 курс мифи/2 сесместр/структура данных/compf_result/test_roman_compf.py"])