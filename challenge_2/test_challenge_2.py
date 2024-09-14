import pytest
from challenge_2 import solution

def test_solution_empty_input():
    # Test with empty data centers list
    assert solution([], 0) == 0
    assert solution([], 1) == None

def test_solution_single_element():
    # Test with a single data center
    assert solution([1], 0) == 0
    assert solution([1], 5) == 1  # All fragments can be assigned to risk factor 1 without increasing risk
    assert solution([10], 3) == 1000  # 10^3 = 1000

def test_solution_multiple_centers():
    # Test with multiple data centers
    assert solution([10, 20, 30], 5) == 400  # Optimal distribution: [2, 2, 1]
    assert solution([2, 3, 5], 10) == 32  # Optimal distribution: [5, 3, 2]
    assert solution([4, 6, 8], 7) == 64  # Optimal distribution: [3, 2, 2]

def test_solution_large_fragments():
    # Test with a large number of fragments
    assert solution([2, 3, 5], 20) == 1024  # Optimal distribution: [10, 6, 4]

def test_solution_high_risk_factors():
    # Test with high risk factors
    assert solution([100, 200, 300], 2) == 200  # Optimal distribution: [1, 1, 0]

def test_solution_high_number_of_fragments():
    # Test with a very high number of fragments
    assert solution([1, 2, 3, 5], 100000) == 1  # All fragments assigned to risk factor 1 (takes a bit of time)
