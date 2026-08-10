class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        seen = set()
        longest = 0

        if len(s) <= 1:
            return len(s)

        seen.add(s[left])

        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
        return longest