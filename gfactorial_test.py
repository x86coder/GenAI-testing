'''
PROMPT: Output: file containing the code, using PyTest framework style and using just integer numbers for the function. Input: Can you please generate a few test cases for my function gfactorial(x) ?
Copilot model: GPT-4.1
'''
import pytest
from gfactorial import gfactorial

def test_gfactorial_zero():
    assert gfactorial(0) == 1

def test_gfactorial_one():
    assert gfactorial(1) == 1

def test_gfactorial_three():
    assert gfactorial(3) == 6

def test_gfactorial_six():
    assert gfactorial(6) == 720

def test_gfactorial_negative_integer():
    with pytest.raises(ValueError):
        gfactorial(-1)