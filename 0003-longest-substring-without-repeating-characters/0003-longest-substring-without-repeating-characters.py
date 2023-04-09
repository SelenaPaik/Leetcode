
# [Previous Solution]
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#        # sliding window, using l and r pointer
#         charSet = set()
#         res = 0
#         l = 0
# 
#         for r in range(len(s)):
#             while(s[r] in charSet):
#                 charSet.remove(s[l])
#                 l +=1
#             charSet.add(s[r])
#             res = max(res, r-l+1)
# 
#         return res
# 
#         
# intuition
# two pointers l,r -> while
# 
# for each character:
#     if character is not in the set:
#         add character to the set
#         r+=1
#         
#     else:
#         compare count to the max
#         keep max(curmax, r-l)
#         initialize pointers(l = r+1, r = l+1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r  = 0,1
        curmax = 0
        charset = set()
        if len(s)==0: return 0
        if len(s)==1: return 1
        charset.add(s[l])
        while(r<len(s)):
            if s[r] not in charset:
                charset.add(s[r])
                r+=1
            else:
                charset.clear()
                curmax = max(curmax, r-l)
                l += 1
                r = l+1
                charset.add(s[l])
        curmax = max(curmax, r-l)        
        return curmax
                
            