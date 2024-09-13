import pytest
from challenge_3 import solution

def test_solution_empty_input():
    assert solution([], []) == None

def test_solution_single_element():
    assert solution([1], [1]) == None
