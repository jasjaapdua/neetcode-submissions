class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [1] * len(nums)
        product_right = [1] * len(nums)
    

        for i in range(1, len(nums)):
            product_left[i] = product_left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            product_right[i] = product_right[i + 1] * nums[i + 1]

        print(product_left)
        print(product_right)
        result = []

        for right, left in zip(product_left, product_right):
            result.append(right * left)
        
        return result