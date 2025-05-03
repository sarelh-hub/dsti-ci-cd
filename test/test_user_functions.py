import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src']

import pytest
import io
from user_functions import *


def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce,wayne2wayneenterprises,com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('brucewayne@wayneenterprises,com'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce.wayne@wayneenterprisescom'))
    assert get_email_from_input() == 'bruce.wayne@wayneenterprisescom'

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py

def test_user_name_input_with_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Sa ra'))
    assert get_user_name_from_input() is None

def test_user_name_input_empty_string(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
    assert get_user_name_from_input() is None

def test_user_name_input_greater_20(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('abcdefgh123456789101112134151617121314151617181920'))
    assert get_user_name_from_input() is None

def test_user_name_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Sara'))
    assert get_user_name_from_input() == "Sara"

def test_password_input_less_eight_ch_no_number_no_special_ch(monkeypatch):
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    monkeypatch.setattr('sys.stdin', io.StringIO('azerty'))
    assert get_password_from_input() is None

def test_password_input_correct(monkeypatch):
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    monkeypatch.setattr('sys.stdin', io.StringIO('azerty1+'))
    assert get_password_from_input() == "azerty1+"

