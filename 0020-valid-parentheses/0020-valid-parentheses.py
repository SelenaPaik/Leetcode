# put (,[,{ in a stack
# pop when ),],} comes
       


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s)==1: return False
        if s[0]==")" or s[0]=="}" or s[0]=="]": return False
        for i in range(len(s)):

            if s[i] =="(" or s[i] =="[" or s[i] =="{":
                stack.append(s[i])
            else:
                if len(stack)>0:
                    if (s[i] == ")" and stack[-1]=="(") or (s[i] == "}" and stack[-1]=="{") or (s[i] == "]" and stack[-1]=="["):
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    if s[i] =="]" or s[i] =="}" or s[i] ==")":
                         stack.append(s[i])
        if len(stack)==0: 
            return True
        else: 
            return False
        