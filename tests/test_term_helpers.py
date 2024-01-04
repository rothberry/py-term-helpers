import pytest
from src.py_term_helpers import TermHelper
# needs the '-s' flag to run


def test_star_line():
    assert not TermHelper.star_line()


def test_kv_print():
    my_dict = {'key': "value"}
    TermHelper.kv_print(my_dict)
    # breakpoint()
