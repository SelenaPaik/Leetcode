
# [First trial]
# brute force : time limit exceeded
# 
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         ans =[]
#         for i in range(0,len(numbers)):
#             tmp = target - numbers[i]
#             for j in range(i+1, len(numbers)):
#                 if tmp == numbers[j]:
#                     ans.append(i+1)
#                     ans.append(j+1)
#                     return ans
#         return ans
# 
#     
# [Second trial]
# 
# use pointer in each side r,l
# utilize 'sorted' feature -> if sum is too big, l--, if sum is to small, r ++
# find 2 numbers
# 


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers)-1
        while r<l :
            if numbers[r] + numbers[l] > target:
                l-=1
            elif numbers[r] + numbers[l] < target:
                r+=1
            elif numbers[r] + numbers[l] == target:
                return [r+1,l+1]
        