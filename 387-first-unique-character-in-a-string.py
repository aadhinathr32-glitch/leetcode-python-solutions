"""Return the first character that occurs once, or None if none exists.

Approach: count characters, then scan in original order.
Time: O(n). Space: O(k).
"""
from collections import Counter

def first_non_repeating(text: str) -> str | None:
    counts = Counter(text)
    for character in text:
        if counts[character] == 1:
            return character
    return None

if __name__ == "__main__":
    assert first_non_repeating("swiss") == "w"
    assert first_non_repeating("aabb") is None
    assert first_non_repeating("x") == "x"
    assert first_non_repeating("") is None
    print("All First Non-Repeating Character examples passed.")
