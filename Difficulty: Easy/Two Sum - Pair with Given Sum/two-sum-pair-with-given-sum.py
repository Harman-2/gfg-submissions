class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()
		l, r = 0, len(arr)-1
		while l<r:
		    if arr[l]+arr[r]==target:
		        return True
		    elif arr[l]+arr[r]<target:
		        l +=1
		    else:
		        r -=1
	    return False