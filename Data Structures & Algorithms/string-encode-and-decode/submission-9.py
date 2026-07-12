class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            wordlen = len(word)
            encoded = f"{encoded}{wordlen}#{word}"
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            length = 0
            while s[i] in '0123456789':
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            print(length)
            word = s[i: i+length]
            print(word)
            result.append(word)
            i+= length
        return result


