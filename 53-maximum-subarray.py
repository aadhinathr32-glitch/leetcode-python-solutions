"""Return the largest sum of a non-empty contiguous subarray.

Approach: Kadane's algorithm.
Time: O(n). Space: O(1).
"""
def max_subarray_sum(values: list[int]) -> int:
    if not values:
        raise ValueError("values must not be empty")
    current = best = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

if __name__ == "__main__":
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([-5, -2, -8]) == -2
    assert max_subarray_sum([3]) == 3
    print("All Maximum Subarray Sum examples passed.")
