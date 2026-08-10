class Solution:
    def convertToCamelCase(self, s: str) -> str:
        words = s.split()
        return words[0] + ''.join(w.capitalize() for w in words[1:])