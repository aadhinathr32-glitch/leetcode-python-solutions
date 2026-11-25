class Solution:
    def bestTeamScore(self, scores, ages):
        players = sorted(zip(ages, scores))

        n = len(players)
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]

        for i in range(n):
            for j in range(i):
                # Previous player's score must not be greater
                # than current player's score.
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)
