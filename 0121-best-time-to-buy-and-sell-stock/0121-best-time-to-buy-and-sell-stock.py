
# brute force, use pointer -> time limit exceeded
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l,r = 0, 1
#         ans =[]
#         for i in range(0, len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 res = prices[j]-prices[i]
#                 ans.append(res)
#         if len(ans)>0:        
#             res = max(ans)
#         else:
#             res = 0
#         if res >0:
#             return res
#         else:
#             return 0
#         
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

            