# [intuition]
# use stack 
# if operator:
#     pop 2 numbers and calculate, truncate(int)
# 
# if number:
#     put in stack
# 
# string to operator


def operations(num1:int, num2:int, op:str) -> int:
        if op == '+':
            return int(num1 + num2)
        if op == '-':
            return int(num1 - num2)
        if op == '*':
            return int(num1 * num2)
        if op == '/':
            return math.trunc(num1 / num2)
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in ["+", "-", "*", "/"]:
                op2 = stack.pop()
                op1 = stack.pop()
                res = operations(op1,op2,char)
                stack.append(int(res))
            else:
                stack.append(int(char))
        return stack.pop()
            
                
                
                
  