from lesson import *
import pytest


def test_answer():
    assert add_one(7) == 8


def test_division():
    assert division(4, 2) == 2.0, 'OOPS'


def test_division2():
    with pytest.raises(ZeroDivisionError):
        division(4, 0)


def test_palindrom():
    test_case = [('hello', False), ('mom', True), ('ololo', True), ('makers', False)]
    for case in test_case:
        assert is_palindrom(case[0]) == case[1]