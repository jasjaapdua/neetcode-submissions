class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in seen: 
                # this means that it is a valid sequence start
                k = 1
                while (n + k) in seen:
                    k += 1
                longest = max(k, longest)
        return longest