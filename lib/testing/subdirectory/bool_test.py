#!/usr/bin/env python3

from bool_functions import return_true

def test_return_true():
    '''In bool_functions, function "return_true" returns True.'''
    print("Function output:", return_true())  # Prints the actual return value
    assert return_true() == False  # Assertion for pytest
