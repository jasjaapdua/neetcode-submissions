class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        print(left)
        print(nums[left], target, nums[-1])
        if nums[left] <= target and target <= nums[-1]:
            print("searching right half")
            left, right = left, len(nums) - 1
        else:
            print("searching left half")
            left, right = 0, left - 1
        
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1