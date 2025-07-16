'''
IDE Input: gfibonacci_test.py
PROMPT: Output: another test class or another generated file. Input: Thanks. aside from that. I feel the test cases in my TestGfibonacci class are brief. Can you wirte more test cases and consider extreme cases and/or edge cases? So I can be sure the function won't break.
'''
import pytest
from gfibonacci import gfibonacci

class TestGfibonacciEdgeCases:
    def test_zero_term(self):
        # Depending on intended behavior, this may raise an error or return a value.
        # Here, let's check if it raises an IndexError or ValueError.
        with pytest.raises(Exception):
            gfibonacci(0)

    def test_negative_term(self):
        with pytest.raises(Exception):
            gfibonacci(-5)

    def test_large_input(self):
        # Test a large input for performance and correctness
        assert gfibonacci(20) == 4181
        assert gfibonacci(30) == 514229

    def test_consecutive_terms(self):
        # Check that the difference between consecutive terms matches Fibonacci property
        for i in range(3, 15):
            assert gfibonacci(i) == gfibonacci(i-1) + gfibonacci(i-2)

    def test_type_error_on_non_integer(self):
        with pytest.raises(TypeError):
            gfibonacci(3.5)
        with pytest.raises(TypeError):
            gfibonacci("5")