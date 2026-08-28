class Solution:
    def fibonacciNumbers(self, n: int) -> list[int]:
        # code here
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0,1]
        res = self.fibonacciNumbers(n-1)
        res.append(res[-1]+res[-2])
        return res