class Solution:
    def getDistances(self, arr):
        positions = {}

        # Store indices for each value
        for i, num in enumerate(arr):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        answer = [0] * len(arr)

        # Calculate the sum of distances for each occurrence
        for indices in positions.values():
            total_sum = sum(indices)
            prefix_sum = 0

            for j, i in enumerate(indices):
                left_count = j
                right_count = len(indices) - j - 1

                left_sum = prefix_sum
                right_sum = total_sum - prefix_sum - i

                answer[i] = (
                    i * left_count - left_sum
                    + right_sum - i * right_count
                )

                prefix_sum += i

        return answer


solution = Solution()
assert solution.getDistances([2, 1, 3, 1, 2, 3, 3]) == [4, 2, 7, 2, 4, 4, 5]
assert solution.getDistances([10, 5, 10, 10]) == [5, 0, 3, 4]
print("All sample tests passed.")
