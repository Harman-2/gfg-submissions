class Solution:
    def evaluatePostfix(self, arr):
        stack = []
        operators = { '+', '-', '*', '/', '^'}
        
        for element in arr:
            if element not in operators:
                stack.append(int(element))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                
                if element == '+':
                    stack.append(val1+val2)
                elif element == '-':
                    stack.append(val1 - val2)
                elif element == '*':
                    stack.append(val1 * val2)
                elif element == '/':
                    stack.append(val1//val2)
                elif element == '^':
                    stack.append(val1**val2)
        return stack[0]
                
                
                
        
        