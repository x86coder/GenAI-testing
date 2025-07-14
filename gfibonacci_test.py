'''
PROMPT: Output: file containing the resulting code and using PyTest's framework code style. Input: Can you please generate a few test cases (inside a Test Class) for my function gfibonacci(i) ? Context: fibonacci(i) is a function which returns the i-th member (or member number i) in the Fibonacci's sucession. The first member is 0, and the second is 1 in this case.
'''

import pytest
from gfibonacci import gfibonacci

class TestGfibonacci:
    def test_first_term(self):
        assert gfibonacci(1) == 0

    def test_second_term(self):
        assert gfibonacci(2) == 1

    def test_third_term(self):
        assert gfibonacci(3) == 1

    def test_fifth_term(self):
        assert gfibonacci(5) == 3

    def test_seventh_term(self):
        assert gfibonacci(7) == 8

    def test_large_term(self):
        assert gfibonacci(10) == 34