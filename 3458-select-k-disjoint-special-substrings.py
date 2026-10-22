"""
LeetCode 3458: Select K Disjoint Special Substrings

For each character, expand the interval starting at its first occurrence
until every character inside the interval has all of its occurrences
contained within it. These are candidate special substrings.
Then greedily select non-overlapping intervals by earliest ending position.

Time Complexity: O(26 * n + 26 log 26), effectively O(n)
Space Complexity: O(26), effectively O(1)
"""


class Solution:
    def maxSubstringLength(self, s, k):
        if k == 0:
            return True

        n = len(s)
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch in first:
            start = first[ch]
            end = last[ch]
            i = start
            valid = True

            while i <= end:
                c = s[i]
                if first[c] < start:
                    valid = False
                    break
                end = max(end, last[c])
                i += 1

            if valid and not (start == 0 and end == n - 1):
                intervals.append((start, end))

        intervals.sort(key=lambda interval: interval[1])

        count = 0
        previous_end = -1

        for start, end in intervals:
            if start > previous_end:
                count += 1
                previous_end = end
                if count >= k:
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSubstringLength("abcdbaefab", 2) is True
    assert solution.maxSubstringLength("cdefdc", 3) is False
    assert solution.maxSubstringLength("abeabe", 0) is True

    print("All sample tests passed.")
