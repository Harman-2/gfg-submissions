class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        for i in range ((n-2)// 2+1):
            l = 2 * i + 1
            r = 2 * i + 2
            
            if l < n and arr[l]>arr[i]:
                return False
            if r < n and arr[r]>arr[i]:
                return False
        return True
        