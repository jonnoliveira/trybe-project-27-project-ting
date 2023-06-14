import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    test = PriorityQueue()

    assert test.__len__() == 0

    test.enqueue({"qtd_linhas": 1})
    test.enqueue({"qtd_linhas": 2})
    test.enqueue({"qtd_linhas": 3})
    test.enqueue({"qtd_linhas": 4})

    test.enqueue({"qtd_linhas": 5})
    test.enqueue({"qtd_linhas": 61})
    test.enqueue({"qtd_linhas": 71})
    test.enqueue({"qtd_linhas": 91})

    assert test.__len__() == 8
    assert len(test.high_priority) == 4
    assert len(test.regular_priority) == 4

    test.dequeue()
    test.dequeue()

    assert test.__len__() == 6
    assert test.search(0) == {"qtd_linhas": 3}
    assert test.search(5) == {"qtd_linhas": 91}

    with pytest.raises(IndexError):
        test.search(777)
