class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        if len(s) == 0:
            return 0

        left, right = 0, 1
        result = 0
        count = set()
        count.add(s[left])
        result = len(count)

        while right < len(s):
            if s[right] not in count:
                count.add(s[right])
                right += 1
                result = max(result, len(count))
            else:
                while s[left] != s[right]:
                    count.remove(s[left])
                    left += 1
                count.remove(s[left])
                left += 1
        
        return result
            

        