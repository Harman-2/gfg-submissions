class Solution:
    def checkPangram(self,s):
        seen = set()
        for char in s:
            if 'a'<=char<='z' or 'A'<=char <='Z':
                seen.add(char.lower())
        return len(seen) == 26