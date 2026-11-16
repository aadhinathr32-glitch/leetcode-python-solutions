import heapq


class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        shortest = [float("inf")] * n
        ways = [0] * n

        shortest[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > shortest[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                if new_time < shortest[neighbor]:
                    shortest[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_time, neighbor))

                elif new_time == shortest[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]


solution = Solution()
assert solution.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]) == 4
assert solution.countPaths(2, [[1,0,10]]) == 1
print("All sample tests passed.")
