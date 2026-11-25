"""Check whether text is a palindrome ignoring non-alphanumeric characters and case.

Time: O(n). Auxiliary space: O(1) for the two-pointer scan.
"""
def is_valid_palindrome(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].casefold() != text[right].casefold():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    assert is_valid_palindrome("A man, a plan, a canal: Panama")
    assert is_valid_palindrome("")
    assert not is_valid_palindrome("race a car")
    print("All Valid Palindrome examples passed.")
