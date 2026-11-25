"""Merge overlapping intervals.

Sort then merge in one pass. Time: O(n log n). Space: O(n) for the result.
"""
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted((interval[0], interval[1]) for interval in intervals)
    merged: list[list[int]] = []
    for start, end in ordered:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([]) == []
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[5, 7]]) == [[5, 7]]
    print("All Merge Intervals examples passed.")
