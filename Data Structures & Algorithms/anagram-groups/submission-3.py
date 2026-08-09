class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        result_map = {}

        def get_freq_list(word):
            freq_list = [0] * 26
            for char in word:
                freq_list[ord(char) - 97] += 1
            return tuple(freq_list)
        

        for word in strs:
            freq_list = get_freq_list(word)
            if freq_list in result_map:
                result_map[freq_list].append(word)
            else:
                result_map[freq_list] = [word]
            
        for key in result_map:
            result.append(result_map[key])
        
        return result
