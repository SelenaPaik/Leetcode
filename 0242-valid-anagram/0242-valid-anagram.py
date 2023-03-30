
# use dictionary(key-value : character-count)
# 
# 1. put every character and the count of each character in s in the data structure
# 2. subtract 1 from every character in t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        for c in s:
            d[c] = 0
        
        for c in s:
            d[c] +=1
        
        for c in t:
            if d.get(c) == None: return False
            else:
                d[c] -= 1
        
        for key in d:
            if d[key] != 0:
                return False
            
        return True