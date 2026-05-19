class Solution:
    def minWindow(self, s: str, t: str) -> str:
        random_max = 9999999999999999

        if len(s) < len(t):
            return ""

        shortest = random_max
        short_start = 0
        def checkValid(s_map, t_map):
            for key in t_map:
                if s_map[key] < t_map[key]:
                    return False
            return True
        
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in t:
            t_map[c] += 1
        
        left, right = 0, 0

        while right < len(s):
            while not checkValid(s_map, t_map) and right < len(s):
                s_map[s[right]] += 1
                right += 1
            
            # we have a valid solution now
            while checkValid(s_map, t_map):
                if shortest > (right - left):
                    short_start = left
                    shortest = right - left
                
                s_map[s[left]] -= 1
                left += 1
        
        if shortest == random_max:
            return ""
        return s[short_start: short_start + shortest]
        