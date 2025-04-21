
from pytest import raises
from hex_calc import HexCalc


class TestHexCalc:
    def setup_method(self):
        self.c = HexCalc()

    def test_hex_numbers(self):
        assert self.c.compile("0xA") == 10
        assert self.c.compile("0X1F") == 31

    def test_min_priority_multiplication(self):
        assert self.c.compile("0xA+0x2*0x3") == 16  # 10 + (2*3) = 16
        assert self.c.compile("0x10/0x4-0x2") == 2  # (16/4)-2 = 2

    def test_complex_expressions(self):
        assert self.c.compile("0x1F*(0xA-0x2)/0x4") == 62  # 31*(10-2)/4 = 62

    def test_errors(self):
        with raises(ValueError):
            self.c.compile("0xG")  # Недопустимый символ
        with raises(ValueError):
            self.c.compile("0x4000")  # Превышение максимального значения
        with raises(ValueError):
            self.c.compile("")  # Пустая строка


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "/Users/maksim/Desktop/1 курс мифи/2 сесместр/структура данных/compf_result/test_hex_calc.py"])