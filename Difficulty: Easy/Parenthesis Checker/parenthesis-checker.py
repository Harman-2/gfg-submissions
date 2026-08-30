class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        map= { ')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c in map:
                if not stack:
                    return False
                top_ele = stack.pop() 
                if map[c] != top_ele:
                    return False
            else:
                stack.append(c)
        return not stack

            
        
        