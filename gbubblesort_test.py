'''
PROMPT: Output: file containing the resulting code and using PyTest's framework code style. Try to include different combinations of numbers (lists). Test edge cases too. Input: Can you please generate a few test cases (inside a Test Class) for my function gbubblesort(list) ?
'''
import pytest
from gbubblesort import gbubblesort

class TestGbubblesort:
    def test_sorted_list(self):
        assert gbubblesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_list(self):
        assert gbubblesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_unsorted_list(self):
        assert gbubblesort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert gbubblesort([2, 3, 2, 1, 1]) == [1, 1, 2, 2, 3]

    def test_single_element(self):
        assert gbubblesort([42]) == [42]

    def test_empty_list(self):
        assert gbubblesort([]) == []

    def test_all_equal(self):
        assert gbubblesort([7, 7, 7, 7]) == [7, 7, 7, 7]