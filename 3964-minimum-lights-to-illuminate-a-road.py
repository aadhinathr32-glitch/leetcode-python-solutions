class Solution:
    def minLights(self, lights):
        n = len(lights)

        # Difference array for existing bulb coverage
        diff = [0] * (n + 1)

        # Mark the range illuminated by each existing bulb
        for i, v in enumerate(lights):
            if v > 0:
                left = max(0, i - v)
                right = min(n, i + v + 1)

                diff[left] += 1
                diff[right] -= 1

        answer = 0
        coverage = 0

        # Scan from left to right
        for i in range(n):
            coverage += diff[i]

            # Current position is not illuminated
            if coverage == 0:
                answer += 1

                # Place the new bulb at i + 1.
                # It covers i, i + 1, and i + 2.
                coverage += 1

                if i + 3 <= n:
                    diff[i + 3] -= 1

        return answer


solution = Solution()
assert solution.minLights([0, 0, 0, 0]) == 2
assert solution.minLights([0, 0, 0, 2, 0]) == 1
print("All sample tests passed.")
