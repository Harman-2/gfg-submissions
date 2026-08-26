class Solution:
    def isSubset(self, a, b):
        # code here
        a.sort()
        b.sort()
        i = 0 
        j = 0
        while i<len(a) and j <len(b):
            if a[i]==b[j]:
                j+=1
                i +=1
            elif a[i]<b[j]:
                i+=1
            else:
                return False
        return j == len(b)
        
    
    
    
    
