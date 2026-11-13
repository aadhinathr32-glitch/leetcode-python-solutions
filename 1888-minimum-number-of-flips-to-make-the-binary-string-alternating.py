class Solution:
    def minFlips(self, s):
        n = len(s)

        # Compare with both possible alternating patterns.
        # Pattern 1: 010101...
        # Pattern 2: 101010...
        diff1 = 0
        diff2 = 0

        # Double the string to simulate all rotations.
        s = s + s

        answer = n

        for i in range(2 * n):
            if s[i] != ("0" if i % 2 == 0 else "1"):
                diff1 += 1
            else:
                diff2 += 1

            # Remove the character that leaves the window.
            if i >= n:
                if s[i - n] != ("0" if (i - n) % 2 == 0 else "1"):
                    diff1 -= 1
                else:
                    diff2 -= 1

            # Once the window has size n, check the answer.
            if i >= n - 1:
                answer = min(answer, diff1, diff2)

        return answer


solution = Solution()

assert solution.minFlips("111000") == 2
assert solution.minFlips("010") == 0
assert solution.minFlips("1110") == 1

print("All sample tests passed.")
