import heapq


class Solution:
    def longestDiverseString(self, a, b, c):
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        result = []

        while heap:
            count, char = heapq.heappop(heap)

            # Avoid creating three consecutive identical characters.
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                if not heap:
                    break

                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))

                heapq.heappush(heap, (count, char))
            else:
                result.append(char)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, char))

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.longestDiverseString(1, 1, 7)
    assert len(result1) == 8
    assert "aaa" not in result1 and "bbb" not in result1 and "ccc" not in result1
    assert result1.count("a") <= 1
    assert result1.count("b") <= 1
    assert result1.count("c") <= 7

    assert solution.longestDiverseString(7, 1, 0) == "aabaa"
    assert solution.longestDiverseString(0, 0, 1) == "c"

    print("All sample tests passed.")
