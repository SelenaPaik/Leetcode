

# intuition: consider 0 -> count the number of 0
# 
# 1. brute force: not efficient to conduct production every time
# 2. divide the case:
#     if 0 exists:
#         # of 0s = 1 : put 0 into everywhere except for 0 position
#         # of 0s > 1 : put 0 into everywhere
#     if not: 
#         multiply every element and divide by arr[i]

    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocnt = 0
        mul = 1
        ans = []
        
        for num in nums:
            if num != 0:
                mul *= num
        
        for num in nums:    
            if num == 0:
                zerocnt += 1
        
        for num in nums:
            if zerocnt == 0:
                res = int(mul/num)
                ans.append(res)
            elif zerocnt == 1:
                if num == 0:
                    ans.append(mul)
                else:
                    ans.append(0)
            else:
                ans.append(0)
               
            
        return ans