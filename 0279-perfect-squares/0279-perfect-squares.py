class Solution:
    def numSquares(self, n: int) -> int:

        # dp[i] will hold the least number of perfect squares summing to i
        dp = [0] + [float('inf')] * n

        # precompute all perfect squares <= n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # bottom-up fill
        for target in range(1, n + 1):
            for sq in squares:
                if sq > target:
                    break
                dp[target] = min(dp[target], dp[target - sq] + 1)

        return dp[n]