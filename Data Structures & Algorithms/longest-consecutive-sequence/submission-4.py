class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if (num - 1) not in seen:
                k = 1
                while (num + k) in seen:
                    k += 1
                longest = max(longest, k)
        return longest
