"""
https://www.guru99.com/pytest-tutorial.html
练习 py test

https://docs.pytest.org/en/stable/index.html
官网地址
"""

# noinspection PyUnresolvedReferences
import pytest


def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"


"""
pytest pytest_demo01.py 

================================================================= test session starts =================================================================
platform darwin -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/moqi/Code/python-algorithm/learn/pytest
collected 2 items                                                                                                                                     

pytest_demo01.py F.                                                                                                                             [100%]

====================================================================== FAILURES =======================================================================
_________________________________________________________________ test_file1_method1 __________________________________________________________________

    def test_file1_method1():
        x = 5
        y = 6
        assert x + 1 == y, "test failed"
>       assert x == y, "test failed"
E       AssertionError: test failed
E       assert 5 == 6

pytest_demo01.py:14: AssertionError
=============================================================== short test summary info ===============================================================
FAILED pytest_demo01.py::test_file1_method1 - AssertionError: test failed
============================================================= 1 failed, 1 passed in 0.04s =============================================================

"""
