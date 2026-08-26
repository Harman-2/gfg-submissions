class Solution:
    def minRemove(self, a, b):
        count_a={}
        count_b = {}
        for x in a:
            count_a[x] = count_a.get(x, 0) + 1
        for x in b:
            count_b[x] = count_b.get(x,0) + 1
        removals = 0
        for x in count_a:
            if x in count_b:
                removals += min(count_a[x], count_b[x])
        return removals
        
       
