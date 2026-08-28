class Solution:
    def factorial(self, n: int) -> int:
        # code here
        res = 1
        for i in range(1, n+1):
            res *= i 
        return res
        