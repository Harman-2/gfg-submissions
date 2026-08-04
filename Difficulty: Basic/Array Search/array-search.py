class Solution:
    def search(self,arr, x):
        for i in range(0, len(arr), 1):
            if arr[i]==x:
                return i
        return -1