class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = f"{encoded}{len(word)}#{word}" 
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            wordlen = 0
            while s[i] in "1234567890":
                wordlen = wordlen * 10 + int(s[i])
                i += 1
            i += 1
            word = s[i: i + wordlen]
            decoded.append(word)
            i += wordlen
        return decoded