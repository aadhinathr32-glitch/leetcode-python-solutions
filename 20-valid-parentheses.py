"""Check whether brackets are correctly nested.

Time: O(n). Space: O(n).
"""
def is_valid_parentheses(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
        else:
            return False
    return not stack

if __name__ == "__main__":
    assert is_valid_parentheses("([]{})")
    assert is_valid_parentheses("")
    assert not is_valid_parentheses("(]")
    assert not is_valid_parentheses("(((")
    print("All Valid Parentheses examples passed.")
