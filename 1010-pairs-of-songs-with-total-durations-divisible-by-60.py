class Solution:
    def numPairsDivisibleBy60(self, time):
        remainder_count = [0] * 60
        pairs = 0

        for duration in time:
            remainder = duration % 60
            complement = (60 - remainder) % 60

            pairs += remainder_count[complement]
            remainder_count[remainder] += 1

        return pairs


if __name__ == "__main__":
    solution = Solution()

    assert solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
    assert solution.numPairsDivisibleBy60([60, 60, 60]) == 3

    print("All sample tests passed.")
