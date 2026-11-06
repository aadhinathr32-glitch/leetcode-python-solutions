class Solution:
    def longestEqualSubarray(self, nums, k):
        positions = {}

        # Store the indices where each value appears.
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        max_length = 0

        # Process each distinct value.
        for pos in positions.values():
            left = 0

            for right in range(len(pos)):
                # Number of elements between the two occurrences
                # that are not equal to the current value.
                while pos[right] - pos[left] - (right - left) > k:
                    left += 1

                max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()

assert solution.longestEqualSubarray([1, 3, 2, 3, 1, 3], 3) == 3
assert solution.longestEqualSubarray([1, 1, 2, 2, 1, 1], 2) == 4

print("All sample tests passed.")
