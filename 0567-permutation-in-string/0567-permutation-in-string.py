# intuition
# 1. dictionary: count the number of each alphabet in s1
# 2. if character in s2 exists in dictionary, count -=1
# 3. else, check next character(do nothing)
# 4. when every values in dictionary are 0, return True

# use sliding window, window size = len(s1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}

        for c in s1:
            if c in dic1:
                dic1[c] += 1
            else:
                dic1[c] = 1
                
        for l in range(len(s2) - len(s1) + 1):
            dic2 = {}
            for i in range(l, l + len(s1)):
                if s2[i] in dic2:
                    dic2[s2[i]] += 1
                else:
                    dic2[s2[i]] = 1
            if dic1 == dic2:
                return True
                
        return False
                
        
       
                
            