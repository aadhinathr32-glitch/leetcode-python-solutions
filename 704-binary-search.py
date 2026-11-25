"""Find target in a sorted ascending list; return its index or -1.

Time: O(log n). Space: O(1).
"""
def binary_search(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 2) == -1
    assert binary_search([], 4) == -1
    assert binary_search([5], 5) == 0
    print("All Binary Search examples passed.")
