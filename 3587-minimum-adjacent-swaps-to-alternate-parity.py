class Solution:
    def minSwaps(self, nums):
        even_positions = []
        odd_positions = []

        # Store the positions of even and odd numbers
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even_positions.append(i)
            else:
                odd_positions.append(i)

        # Impossible if the difference is greater than 1
        if abs(len(even_positions) - len(odd_positions)) > 1:
            return -1

        def calculate_cost(positions):
            cost = 0

            for i, pos in enumerate(positions):
                target = i * 2
                cost += abs(pos - target)

            return cost

        # More evens -> must start with even
        if len(even_positions) > len(odd_positions):
            return calculate_cost(even_positions)

        # More odds -> must start with odd
        if len(odd_positions) > len(even_positions):
            return calculate_cost(odd_positions)

        # Equal numbers -> either parity can start
        even_cost = calculate_cost(even_positions)
        odd_cost = calculate_cost(odd_positions)

        return min(even_cost, odd_cost)


solution = Solution()
assert solution.minSwaps([2, 4, 6, 5, 7]) == 3
assert solution.minSwaps([2, 4, 5, 7]) == 1
assert solution.minSwaps([1, 2, 3]) == 0
assert solution.minSwaps([4, 5, 6, 8]) == -1
print("All sample tests passed.")
