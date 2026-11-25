"""Return each element's product excluding itself, without division.

Time: O(n). Auxiliary space: O(1) excluding the output list.
"""
def product_except_self(values: list[int]) -> list[int]:
    result = [1] * len(values)
    prefix = 1
    for i, value in enumerate(values):
        result[i] = prefix
        prefix *= value
    suffix = 1
    for i in range(len(values) - 1, -1, -1):
        result[i] *= suffix
        suffix *= values[i]
    return result

if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([0, 1, 2]) == [2, 0, 0]
    assert product_except_self([]) == []
    print("All Product Except Self examples passed.")
