from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        res = []
        q = deque()
        for i in range(len(arr)):
            if q and q[0] < i - k + 1:
                q.popleft()
            
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            q.append(i)
            
            if i >= k -1:
                res.append(arr[q[0]])
        return res
        