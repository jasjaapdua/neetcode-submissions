class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        left, right = 0, 1

        if len(s) <= 1:
            return len(s)
        
        seen.add(s[left])
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                result = max(result, right - left)
                left += 1
            else:
                seen.add(s[right])
                result = max(result, right - left + 1)
                right += 1

        return result