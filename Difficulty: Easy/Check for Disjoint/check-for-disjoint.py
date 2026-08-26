class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        #code here
        a.sort()
        b.sort()
        i = 0 
        j = 0
        while i <len(a) and j <len(b):
            if a[i]==b[j]:
                return False
            elif  a[i]<b[j]:
                i += 1
            else:
                j += 1
        return True
                