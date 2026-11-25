"""Remove duplicates while preserving first-occurrence order.

Time: O(n) expected. Space: O(n).
"""
def remove_duplicates(values: list[int]) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

if __name__ == "__main__":
    assert remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert remove_duplicates([]) == []
    assert remove_duplicates([4, 4, 4]) == [4]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    print("All Remove Duplicates examples passed.")
