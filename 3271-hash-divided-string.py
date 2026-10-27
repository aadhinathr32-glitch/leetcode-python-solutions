class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []

        for i in range(0, len(s), k):
            total = 0

            for char in s[i:i + k]:
                total += ord(char) - ord("a")

            hashed_char = total % 26
            result.append(chr(ord("a") + hashed_char))

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.stringHash("abcd", 2) == "bf"
    assert solution.stringHash("mxz", 3) == "i"

    print("All sample tests passed.")
