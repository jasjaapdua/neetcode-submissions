class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def get_freq(s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - 97] += 1
            return freq

        if len(s1) > len(s2):
            return False
        
        s1_freq = get_freq(s1)
        left, right = 0, len(s1) - 1

        s2_freq = get_freq(s2[:len(s1)])
        if s1_freq == s2_freq:
            return True

        while right < len(s2) - 1:
            left_c = s2[left]
            s2_freq[ord(left_c) - 97] -= 1
            left += 1
            right += 1
            right_c = s2[right]
            s2_freq[ord(right_c) - 97] += 1

            if s1_freq == s2_freq:
                return True

            
        return False