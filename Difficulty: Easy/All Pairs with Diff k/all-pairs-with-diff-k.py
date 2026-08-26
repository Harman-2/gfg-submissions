class Solution:
	def countPairs(self, arr, k):
	    freq = {}
	    for num in arr:
	        freq[num]= 1 + freq.get(num,0)
	    count = 0
	    for num in freq:
	        if k == 0:
	            count += freq[num]*(freq[num]-1)//2
	        else:
	            if (num+k) in freq:
	                count+=freq[num]*freq[num+k]
	    return count
    	

