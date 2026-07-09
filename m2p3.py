class Solution:
    def noOfWays(self, m,n,x):
        # code here
        dp = [[0] * (x + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for dice in range(1, n + 1):
            for s in range(1, x + 1):
                ways = 0
                for face in range(1, m + 1):
                    if s >= face:
                        ways += dp[dice - 1][s - face]
                dp[dice][s] = ways

        return dp[n][x]
        