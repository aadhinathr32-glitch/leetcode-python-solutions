from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        result = []

        for char in order:
            result.append(char * counts[char])
            counts[char] = 0

        for char, count in counts.items():
            if count:
                result.append(char * count)

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.customSortString("cba", "abcd") == "cbad"
    assert solution.customSortString("bcafg", "abcd") == "bcad"

    print("All sample tests passed.")
