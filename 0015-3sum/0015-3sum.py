# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         # sort the array
#         nums.sort()
#         
#         for i in range(len(nums)):
#             #skip the loop if there is same number
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             l,r = i+1, len(nums)-1
#             
#             # two sum
#             while (l<r):
#                 threeSum = nums[i] + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r-=1
#                 elif threeSum < 0:
#                     l+=1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])
#                     # not to have same sum
#                     while (l<r and nums[l] == nums[l+1]):
#                         l+=1
#                     while (l<r and nums[r] == nums[r-1]):
#                         r-=1
#                     l+=1
#                     r-=1
#         return res
            
# sort array     
# two sum problem + 1 more element
# for num in nums:
#     use two pointers(r,l) to figure out which element will be sum up to -(num)
#         
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)-2):
                target = -nums[i]
                l,r = i+1, len(nums)-1
                while l<r:
                    if nums[l]+nums[r]< target:
                        l+=1
                    elif nums[l] + nums[r] > target:
                        r-=1
                    elif nums[l] + nums[r] == target:
                        if [nums[i],nums[l],nums[r]] not in ans:
                            ans.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1

        return ans
                
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        