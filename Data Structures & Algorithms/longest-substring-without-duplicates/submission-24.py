class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        seen = set()
        left, right = 0, 1
        seen.add(s[left])
        max_length = 0

        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
        return max_length