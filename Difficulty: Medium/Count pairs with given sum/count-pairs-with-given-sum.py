class Solution:
    def countPairs(self, arr, target):
        #code here
        freq={}
        res = 0 
        for num in arr:
            comp = target - num
            if comp in freq:
                res += freq[comp]
            freq[num] = 1 + freq.get(num, 0)
        return res
                