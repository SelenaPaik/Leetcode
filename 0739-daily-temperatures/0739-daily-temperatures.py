# [Initial Trial]
# sliding window approach -> O(n^2), time limit exceeded
# 73,74,75,71,69,72,76,73
# l  r
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res =[]
#         for l in range(len(temperatures)):
#             r = l+1
#             check = False
#             while r< len(temperatures):
#                 if temperatures[l] < temperatures[r]: 
#                     res.append(r-l)
#                     check = True
#                     break
#                 else:
#                     r+=1
#             if check==False:
#                     res.append(0)
#         return res

# [Second Trial]
# use stack, put index in stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        # put index in stack
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        
        return ans