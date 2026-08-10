class Solution:
    def minWindow(self, s: str, t: str) -> str:
        random_max = 99999999999999999
        if len(s) < len(t):
            return ""

        def check_valid(s_map, t_map):
            for key in t_map:
                if s_map[key] < t_map[key]:
                    return False
            return True
        
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        shortest = random_max
        shortest_start = 0

        for c in t:
            t_map[c] += 1
        
        left, right = 0, 0

        while right < len(s):
            while not check_valid(s_map, t_map) and right < len(s):
                s_map[s[right]] += 1
                right += 1
            
            while check_valid(s_map, t_map):
                if shortest > (right - left):
                    shortest_start = left
                    shortest = right - left
                s_map[s[left]] -= 1
                left += 1
        if shortest == random_max:
            return ""
        return s[shortest_start: shortest_start + shortest]

            
            
        


        