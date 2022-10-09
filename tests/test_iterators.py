import pytest
from scripts.iterators import Queue


def test_for_in():
    q = Queue(collection=[1, 2, 3])
    q_list = []
    for item in q:
        q_list.append(item)

    assert q_list == [1, 2, 3]


def test_list_cast():
    q = Queue(collection=[3, 4, 5])
    lst = [3, 4, 5]

    assert list(q) == lst


def test_len():
    test_range = range(1, 10 + 1)
    q = Queue(collection=test_range)

    assert q.len_ == 10


def test_next():
    test_range = range(1, 5 + 1)
    q = Queue(collection=test_range)

    iterator = iter(q)

    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3


def test_equals():
    q1 = Queue(collection=[1, 2, 3])
    q2 = Queue(collection=[1, 2, 3])

    assert q1 == q2


def test_equals_failure():
    q1 = Queue(collection=[1, 2, 3])
    q2 = Queue(collection=[4, 5, 6])

    assert q1 != q2


def test_comprehension_even():
    test_range = range(1, 10 + 1)
    q = Queue(collection=test_range)

    evens = [num for num in q if num % 2 == 0]

    assert evens == [2, 4, 6, 8, 10]
