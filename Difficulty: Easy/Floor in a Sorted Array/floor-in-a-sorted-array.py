class Solution:
    def findFloor(self, arr, x):
        # code here
        l, r = 0, len(arr)-1
        ans = -1
        
        while l<=r:
            mid = (l+r)//2
            if arr[mid]<=x:
                ans = mid
                l = mid + 1
            else:
                r = mid -1 
        return ans
            
                