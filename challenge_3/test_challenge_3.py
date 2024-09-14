import pytest
from challenge_3 import solution

def test_solution_empty_graph():
    """
    Test with an empty graph. No path should exist.
    """
    graph = {}
    compression_nodes = []
    source = 'A'
    destination = 'B'
    assert solution(graph, compression_nodes, source, destination) == -1

def test_solution_no_path():
    """
    Test with a graph where no path exists between source and destination.
    """
    graph = {
        'A': [('B', 10)],
        'B': [('C', 20)],
        'C': [],
        'D': [('E', 5)]
    }
    compression_nodes = ['B']
    source = 'A'
    destination = 'E'
    assert solution(graph, compression_nodes, source, destination) == -1

def test_solution_same_source_destination():
    """
    Test where source and destination are the same.
    """
    graph = {
        'A': [('B', 10)],
        'B': [('C', 20)],
        'C': []
    }
    compression_nodes = ['B']
    source = 'A'
    destination = 'A'
    assert solution(graph, compression_nodes, source, destination) == 0

def test_solution_compression_beneficial():
    """
    Test where applying compression leads to a lower latency.
    """
    graph = {
        'A': [('B', 5), ('C', 10)],
        'B': [('D', 10)],
        'C': [('D', 6)],
        'D': []
    }
    compression_nodes = ['C']
    source = 'A'
    destination = 'D'
    assert solution(graph, compression_nodes, source, destination) == 13 # Latency: 10 (A -> C) + (6 // 2) (C -> D) = 10 + 3 = 13
