class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        digit_sum = [0] * (n + 1)
        value = [0] * (n + 1)
        count = [0] * (n + 1)

        for i in range(n):
            digit = int(s[i])

            digit_sum[i + 1] = digit_sum[i]
            value[i + 1] = value[i]
            count[i + 1] = count[i]

            if digit != 0:
                digit_sum[i + 1] += digit
                value[i + 1] = (value[i] * 10 + digit) % MOD
                count[i + 1] += 1

        answer = []

        for left, right in queries:
            total_sum = digit_sum[right + 1] - digit_sum[left]
            total_count = count[right + 1] - count[left]

            if total_count == 0:
                x = 0
            else:
                x = (value[right + 1] - value[left] * pow(10, total_count, MOD)) % MOD

            answer.append((x * total_sum) % MOD)

        return answer

solution = Solution()
assert solution.sumAndMultiply("10203004", [[0, 7], [1, 3], [4, 6]]) == [12340, 4, 9]
assert solution.sumAndMultiply("1000", [[0, 3], [1, 1]]) == [1, 0]
assert solution.sumAndMultiply("9876543210", [[0, 9]]) == [444444137]
print("All sample tests passed.")
