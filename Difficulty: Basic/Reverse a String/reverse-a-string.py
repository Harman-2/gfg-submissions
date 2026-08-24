class Solution:
    def reverseString(self, s: str) -> str:
        char_list = []
        for i in range(len(s)-1, -1,-1):
            char_list.append(s[i])
        return"".join(char_list)
        
     