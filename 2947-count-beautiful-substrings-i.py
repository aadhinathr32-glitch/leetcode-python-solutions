"""
LeetCode 2947: Count Beautiful Substrings I

Enumerate every substring while maintaining its vowel and consonant counts.
A substring is beautiful when the counts are equal and their product is
divisible by k.

Time: O(n^2)
Auxiliary space: O(1)
"""


class Solution:
    def beautifulSubstrings(self, s, k):
        vowels_set = set("aeiou")
        total = 0
        n = len(s)

        for start in range(n):
            vowels = 0
            consonants = 0

            for end in range(start, n):
                if s[end] in vowels_set:
                    vowels += 1
                else:
                    consonants += 1

                if vowels == consonants and (vowels * consonants) % k == 0:
                    total += 1

        return total


if __name__ == "__main__":
    solution = Solution()

    assert solution.beautifulSubstrings("baeyh", 2) == 2
    assert solution.beautifulSubstrings("abba", 1) == 3
    assert solution.beautifulSubstrings("bcdf", 1) == 0

    print("All sample tests passed.")
