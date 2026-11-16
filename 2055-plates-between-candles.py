class Solution:
    def platesBetweenCandles(self, s, queries):
        n = len(s)

        # prefix[i] = number of plates before index i
        prefix = [0] * (n + 1)

        # left_candle[i] = nearest candle at or before i
        left_candle = [-1] * n

        # right_candle[i] = nearest candle at or after i
        right_candle = [n] * n

        count = 0
        last = -1

        for i in range(n):
            if s[i] == "*":
                count += 1
            else:
                last = i

            prefix[i + 1] = count
            left_candle[i] = last

        last = n

        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                last = i

            right_candle[i] = last

        answer = []

        for left, right in queries:
            l = right_candle[left]
            r = left_candle[right]

            if l < r:
                answer.append(prefix[r] - prefix[l])
            else:
                answer.append(0)

        return answer


solution = Solution()
assert solution.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]) == [2, 3]
assert solution.platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [9, 0, 0, 0, 0]
print("All sample tests passed.")
