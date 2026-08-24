class Solution:
    def convertToCamelCase(self, s: str) -> str:
        res = []
        cap_next = False
        
        for char in s:
            if char ==' ':
                cap_next=True 
            else:
                if cap_next:
                    res.append(char.upper())
                    cap_next = False 
                else:
                    res.append(char)
        return "".join(res)