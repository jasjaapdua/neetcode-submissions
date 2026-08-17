class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        memo = [0] * (len(nums) + 1)

        def robber(i):
            result = 0
            if memo[i] > 0:
                result = memo[i]
            elif i == 0:
                result = nums[0]
            elif i == 1:
                result = max(nums[0], nums[1])         
            else:
                result = max(
                    nums[i] + robber(i - 2),
                    robber(i - 1)
                )
            memo[i] = result
            return result
        return robber(len(nums) - 1)