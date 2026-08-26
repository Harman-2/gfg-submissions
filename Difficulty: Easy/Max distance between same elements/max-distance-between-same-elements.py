class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        map = {}
        res = 0 
        for i, num in enumerate(arr):
            if num not in map:
                map[num]=i
            else:
                dist = i-map[num]
                if dist>res:
                    res=dist
        return res
        