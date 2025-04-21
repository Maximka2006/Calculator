from pytest import raises
from octal_compf import OctalCompf


class TestOctalCompf: 
    def setup_method(self):
        "Инициализация перед каждым тестом"
        self.c = OctalCompf()
        self.c_right_minus = OctalCompf(right_assoc=["-"])

    def test_valid_numbers(self):
        "Тест корректных чисел"
        assert self.c.compile("10") == "0O12"
        assert self.c.compile("3999") == "0O7637"

        assert self.c_right_minus.compile("10") == "0O12"
        assert self.c_right_minus.compile("3999") == "0O7637"

    def test_invalid_numbers(self):
        "Тест некорректных чисел"
        with raises(ValueError):
            self.c.compile("0")  # Число меньше 1
            self.c_right_minus.compile("0")  # Число меньше 1
        with raises(ValueError):
            self.c.compile("4000")  # Число больше 3999
            self.c_right_minus.compile("4000")  # Число больше 3999

    def test_subtraction_right_associativity(self):
        "Тест правоассоциативности вычитания"

        assert self.c_right_minus.compile("10-5-1") == self.c_right_minus.compile("10-(5-1)")  # Должно быть 10-(5-1) = 6
        assert self.c_right_minus.compile("3-2-1") == self.c_right_minus.compile("3-(2-1)")   # Должно быть 3-(2-1) = 2

    def test_subtraction_left_associativity(self):
        "Тест  левоассоциативности вычитания"
        assert self.c.compile("10-5-1") == "0O12 0O5 - 0O1 -"  # Должно быть 10-(5-1) = 6
        assert self.c.compile("3-2-1") == "0O3 0O2 - 0O1 -"    # Должно быть 3-(2-1) = 2

    def test_mixed_operations(self):
        "Тест смешанных операций"
        assert self.c.compile("2*3+4") == "0O2 0O3 * 0O4 +"      # (2*3)+4 = 12
        assert self.c.compile("(5-2)*3") == "0O5 0O2 - 0O3 *"    # (5-2)*3 = 11

        assert self.c_right_minus.compile("2*3+4") == "0O2 0O3 * 0O4 +"      # (2*3)+4 = 12
        assert self.c_right_minus.compile("(5-2)*3") == "0O5 0O2 - 0O3 *"    # (5-2)*3 = 11

    def test_invalid_symbols(self):
        "Тест недопустимых символов"
        with raises(ValueError):
            self.c.compile("12a+3")  # Недопустимый символ 'a'


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "/Users/maksim/Desktop/1 курс мифи/2 сесместр/структура данных/compf_result/test_octal_compf.py"])  