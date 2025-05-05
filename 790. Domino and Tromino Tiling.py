class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        prefix = [0] * (n + 1)
        prefix[0], prefix[1], prefix[2] = 1, 2, 4  # prefix[i] = sum(dp[0:i+1])

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * prefix[i - 3]) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        return dp[n]
