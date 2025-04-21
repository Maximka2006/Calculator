from pytest import raises
from stack import Stack


class TestStack:


    def setup_method(self):
        self.s = Stack()

    def test_simple1(self):
        assert self.s.array == []

    def test_simple2(self):
        self.s.push(1)
        assert self.s.array == [1]
        a = self.s.pop()
        assert a == 1


    def test_raises(self):
        with raises(Exception):
            self.s.top()
