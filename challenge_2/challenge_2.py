from math import log
from typing import List, Optional

def solution(data_centers: List[int], fragments: int) -> Optional[int]:
    """
    Distributes data fragments across data centers to minimize the maximum risk.

    Args:
        data_centers (List[int]): List of base risk factors for each data center.
        fragments (int): Total number of data fragments to distribute.

    Returns:
        Optional[int]: The minimized maximum risk achievable.
                       Returns None if distribution is not possible.
    """
    # Handle edge cases where allocation is impossible or trivial
    if not data_centers or fragments < 0:
        return None if fragments > 0 else 0

    if fragments == 0:
        return 0  # No risk when no fragments are distributed

    # Sort data centers by their base risk in ascending order
    sorted_centers = sorted(data_centers)

    def can_allocate(max_risk: int) -> bool:
        """
        Determines if it's possible to allocate all fragments such that
        no data center exceeds the specified max_risk.

        Args:
            max_risk (int): The maximum allowable risk for any data center.

        Returns:
            bool: True if allocation is possible within the max_risk constraint, False otherwise.
        """
        total_allocated = 0  # Total fragments that can be allocated without exceeding max_risk
        for base_risk in sorted_centers:
            if base_risk == 1:
                # If base risk is 1, any number of fragments can be assigned without increasing risk
                allocatable = fragments  # Assign as many as needed
            else:
                # Calculate the maximum number of fragments assignable without exceeding max_risk
                if max_risk < 1:
                    allocatable = 0  # Cannot assign any fragments if max_risk is less than 1
                else:
                    # Compute the maximum fragments for this data center
                    allocatable = int(log(max_risk) / log(base_risk))
            # Ensure we don't assign more fragments than needed
            allocatable = min(allocatable, fragments - total_allocated)
            total_allocated += allocatable
            # Early exit if we've already allocated all fragments
            if total_allocated >= fragments:
                return True
        return total_allocated >= fragments

    # Initialize binary search bounds
    left = 1  # Minimum possible risk (when at least one fragment is assigned)
    right = max(base_risk ** fragments for base_risk in data_centers)  # Maximum possible risk

    # Perform binary search to find the minimal maximum risk
    while left < right:
        mid = (left + right) // 2
        if can_allocate(mid):
            right = mid  # Try to find a lower maximum risk
        else:
            left = mid + 1  # Increase the risk since allocation isn't possible

    return left

if __name__ == "__main__":
    # Example usage
    data_centers = [10, 20, 30]
    fragments = 5
    min_risk = solution(data_centers, fragments)
    print(f"Minimized maximum risk: {min_risk}")
