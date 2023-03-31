
# [First Trial]
# intuition: consider 0 -> count the number of 0
# 
# 1. brute force: not efficient to conduct production every time
# 2. divide the case:
#     if 0 exists:
#         # of 0s = 1 : put 0 into everywhere except for 0 position
#         # of 0s > 1 : put 0 into everywhere
#     if not: 
#         multiply every element and divide by arr[i]
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         zerocnt = 0
#         mul = 1
#         ans = []
#         
#         for num in nums:
#             if num != 0:
#                 mul *= num
#         
#         for num in nums:    
#             if num == 0:
#                 zerocnt += 1
#         
#         for num in nums:
#             if zerocnt == 0:
#                 res = int(mul/num)
#                 ans.append(res)
#             elif zerocnt == 1:
#                 if num == 0:
#                     ans.append(mul)
#                 else:
#                     ans.append(0)
#             else:
#                 ans.append(0)
#                
#             
#         return ans


# [Second Trial]
# "without using the division"
# 1. intuition: multiply pre * post
#  pre: 0 ~ i-1
#  post: i+1 ~ len(nums)-1
#   ---> Time limit Exceed
#     
# 2. 
#      [1,2,3,4]
# pre: [1,2,6,24] 
# post:[24,24,12,4]
# 
# ans: [24, 12, 8, 6]
#     
class Solution:
     def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post =[]
        ans=[]
        tmp = 1
        pre.append(1)
        for i in range(0, len(nums)-1):
            pre.append(pre[i] * nums[i])
            
      
        post.append(1)
        for i in range(len(nums)-1,0,-1):
            post.insert(0, post[0] *nums[i])
    
        for i in range(0, len(nums)):
            ans.append(pre[i]*post[i])
            
        return ans

    
