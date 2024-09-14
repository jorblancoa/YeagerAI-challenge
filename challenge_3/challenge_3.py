import heapq
from typing import Dict, List, Tuple

def solution(graph: Dict[str, List[Tuple[str, int]]],
             compression_nodes: List[str],
             source: str,
             destination: str) -> int:
    """
    Determines the path with the lowest total latency between source and destination routers,
    considering possible data compression at specified nodes.

    Args:
        graph (Dict[str, List[Tuple[str, int]]]): Network graph representation.
        compression_nodes (List[str]): Routers where data compression can be applied.
        source (str): Source router ID.
        destination (str): Destination router ID.

    Returns:
        int: The minimum total latency from source to destination.
    """

    # Priority queue: (total_latency, current_node, compression_used)
    heap = [(0, source, False)]

    # TODO:
    # Use a priority queue to keep track of the lowest latency
    # Use a set to keep track of the compression nodes that have been used

    # If destination is unreachable
    return -1

if __name__ == "__main__":
    # Example usage
    graph = {
        'A': [('B', 10), ('C', 20)],
        'B': [('D', 15)],
        'C': [('D', 30)],
        'D': []
    }
    compression_nodes = ['B', 'C']
    source = 'A'
    destination = 'D'
    min_latency = solution(graph, compression_nodes, source, destination)
    print(f"Minimum total latency: {min_latency}")