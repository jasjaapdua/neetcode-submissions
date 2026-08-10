class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        for char in s1:
            s1_freq[ord(char) - 97] += 1
        
        left, right = 0, len(s1) - 1
        s2_freq = [0] * 26
        
        for i in range(0, len(s1)):
            s2_freq[ord(s2[i]) - 97] += 1

        while right < len(s2):
            if s2_freq == s1_freq:
                return True
            s2_freq[ord(s2[left]) - 97] -= 1
            left += 1
            right += 1
            if right == len(s2):
                return False
            s2_freq[ord(s2[right]) - 97] += 1
        return False