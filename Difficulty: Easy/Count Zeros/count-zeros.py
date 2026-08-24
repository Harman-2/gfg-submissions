class Solution:
    def countZeroes(self, arr):
        # code here
        l , r = 0, len(arr)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==0:
                ans = mid
                r = mid -1
            else:
                l = mid +1
        return 0 if ans == -1 else len(arr) - ans
        