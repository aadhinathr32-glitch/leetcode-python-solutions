"""Return indices of two values whose sum equals the target."""

def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of a matching pair, or an empty list if none exists."""
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 7) == []
    print("All Two Sum examples passed.")
