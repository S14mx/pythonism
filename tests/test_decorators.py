import pytest
from scripts.decorators import add_itself, square_itself, multiply_by_three, take_number, add_numbers


def test_add_itself_decorator():
    @add_itself
    def take_number(num):
        return num

    assert take_number(5) == 10


def test_square_itself_decorator():
    @square_itself
    def take_number(num):
        return num
    assert take_number(5) == 25


def test_add_and_square():
    @square_itself
    @add_itself
    def take_number(num):
        return num
    assert take_number(5) == 100


def test_add_numbers_args():

    assert add_numbers(5, 5, 5) == 15


def test_add_numbers_kwargs():

    assert add_numbers(nums=[5, 5, 5]) == 15


def test_add_numbers_multiply_by_three_decorator_args():

    @multiply_by_three
    def add_numbers(*args, **kwargs):
        _sum = 0
        if args:
            for num in args:
                _sum += num
            return _sum
        if kwargs:
            for key, value in kwargs.items():
                for num in value:
                    _sum += num
            return _sum

    assert add_numbers(5, 5, 5) == 45


def test_add_numbers_multiply_by_three_decorator_kwargs():

    @multiply_by_three
    def add_numbers(*args, **kwargs):
        _sum = 0
        if args:
            for num in args:
                _sum += num
            return _sum
        if kwargs:
            for key, value in kwargs.items():
                for num in value:
                    _sum += num
            return _sum

    assert add_numbers(nums=[10, 10, 10]) == 90
