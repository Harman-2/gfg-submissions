
# using FOR loop
'''class Solution:
    def getAlternates(self, arr):
        new = []
        for i in range (0, len(arr), 2):
            new.append(arr[i])
        return new'''
    
# using while loop (i always starts at 0 and then while condition then increment)

'''class Solution:
    def getAlternates(self, arr):
        new =[]
        i = 0
        while i < len(arr):
            new.append(arr[i])
            i += 2
        return new'''

# using slice operator means 0 start, till length ends, then steps --> can't use slice in range of length         

'''class Solution:
    def getAlternates(self, arr):
        return arr[::2]'''
        
# using modulo 

class Solution:
    def getAlternates(self, arr):
        new = []
        for i in range(0, len(arr), 2):
            if i % 2 == 0:
                new.append(arr[i])
        return new