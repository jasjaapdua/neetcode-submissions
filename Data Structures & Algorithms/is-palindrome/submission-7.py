class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()

        s_processed = [
            char for char in s_lower
            if char.isalnum()
        ]

        left = 0
        right = len(s_processed) - 1

        while left < right and s_processed[left] == s_processed[right]:       
            left += 1
            right -= 1
        
        if left < right:
            return False

        return True
        