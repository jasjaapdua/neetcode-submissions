class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in seen_map:
                return [seen_map[required], i]
            
            seen_map[num] = i

