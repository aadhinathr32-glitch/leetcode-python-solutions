"""Determine whether two strings are anagrams.

Approach: compare character-frequency maps.
Time: O(n + m). Space: O(k), where k is the number of distinct characters.
"""
from collections import Counter

def is_anagram(first: str, second: str) -> bool:
    return Counter(first) == Counter(second)

if __name__ == "__main__":
    assert is_anagram("listen", "silent")
    assert is_anagram("aabb", "baba")
    assert not is_anagram("hello", "world")
    assert is_anagram("", "")
    print("All Valid Anagram examples passed.")
