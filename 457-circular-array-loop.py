class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                next_slow = next_index(slow)

                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                next_fast = next_index(fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                next_fast = next_index(next_fast)

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == next_index(slow):
                        break

                    return True

            slow = i

            while nums[slow] != 0:
                if (nums[slow] > 0) != direction:
                    break

                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow

        return False


solution = Solution()
assert solution.circularArrayLoop([2, -1, 1, 2, 2]) is True
assert solution.circularArrayLoop([-1, -2, -3, -4, -5, 6]) is False
assert solution.circularArrayLoop([1, -1, 5, 1, 4]) is True
print("All sample tests passed.")
