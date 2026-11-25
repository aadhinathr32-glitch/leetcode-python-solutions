class Solution:
    def findMaximumNumber(self, k, x):
        def total_price(num):
            total = 0
            bit = x - 1

            while bit < 64:
                one_count = 1 << bit
                cycle = one_count << 1

                full_cycles = (num + 1) // cycle
                remainder = (num + 1) % cycle

                total += full_cycles * one_count
                total += max(0, remainder - one_count)

                if total > k:
                    break

                bit += x

            return total

        left = 0
        right = 10**18

        while left <= right:
            mid = (left + right) // 2

            if total_price(mid) <= k:
                left = mid + 1
            else:
                right = mid - 1

        return right
