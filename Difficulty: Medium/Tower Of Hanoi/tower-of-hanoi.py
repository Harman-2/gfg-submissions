class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        moves = 0
        for i in range(n):
            moves = 2*moves + 1
        return moves