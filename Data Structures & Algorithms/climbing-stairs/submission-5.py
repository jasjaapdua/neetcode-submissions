class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        def climb(n):
            if memo[n] != 0:
                return memo[n]
            if n == 0:
                memo[n] = 1
                return 1
            if n == 1:
                memo[n] = 1
                return 1
            else:
                res = climb(n - 1) + climb(n - 2)
                memo[n] = res
                return res
        return climb(n)
