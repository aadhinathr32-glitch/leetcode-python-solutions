class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= k * threshold:
            count += 1

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]

            if window_sum >= k * threshold:
                count += 1

        return count


# Sample tests
solution = Solution()

assert solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
assert solution.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6

print("All sample tests passed.")
