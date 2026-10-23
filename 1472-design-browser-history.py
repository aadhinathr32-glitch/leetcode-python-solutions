"""LeetCode 1472: Design Browser History

Approach:
- Store visited URLs in a list and track the current page with an index.
- Visiting a new URL removes all forward history.
- Back and forward clamp the index to the valid history range.

Complexity:
- visit: O(n) due to slicing the forward history.
- back: O(1)
- forward: O(1)
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


if __name__ == "__main__":
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.visit("youtube.com")
    assert browser.back(1) == "facebook.com"
    assert browser.back(1) == "google.com"
    assert browser.forward(1) == "facebook.com"
    browser.visit("linkedin.com")
    assert browser.forward(2) == "linkedin.com"
    assert browser.back(2) == "google.com"
    assert browser.back(7) == "leetcode.com"
    print("All sample tests passed.")
