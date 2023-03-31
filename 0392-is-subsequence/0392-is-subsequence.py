
# intuition: go through s and check if every characters are in t
# 
# i = index pointer for s    
# for c in t:
#     if c==s[i]: i ++
# if i==len(s)-1: return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        
        if len(s)==0: return True
       
        for c in t:
            if i>=len(s): break
            if c==s[i]:
                i+=1
        
        if i==len(s):
            return True
        
        return False