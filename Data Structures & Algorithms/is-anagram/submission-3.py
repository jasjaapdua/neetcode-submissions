class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [0] * 26
        t_map = [0] * 26

        for c in s:
            s_map[ord(c) - 97] += 1
        
        for c in t:
            t_map[ord(c) - 97] += 1
        
        return s_map == t_map