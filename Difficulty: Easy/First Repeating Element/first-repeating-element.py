class Solution:
    def firstRepeated(self, arr):
        count = {}
        for num in arr:
            count[num] = 1+count.get(num, 0)
        for i in range(len(arr)):
            if count[arr[i]]>1:
                return i+1
        return -1
     
        