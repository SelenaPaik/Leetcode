# intuition: sort the list, and count the maximum length of sequence
# 
# 1. nums.sort()
# 2. for i in range(1, len(nums)):
#     if nums[i-1]  + 1 == nums[i]:
#         cnt +=1 
#     max update





class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return 1
        nums.sort()
        cnt = 1
        max = 1
        
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                cnt += 1
                if max < cnt:
                    max = cnt
            elif nums[i-1] == nums[i]: continue
            else: cnt = 1
            
            
        return max
    
    
    
    
    
 # if not nums:return 0
 #        if(len(nums)==1): return 1
 #        nums.sort()
 #        fin=[]
 #        res=1
 #        for i in range(1,len(nums)):
 #            if(nums[i-1]+1==nums[i]):
 #                res+=1
 #            elif(nums[i-1]+1<nums[i]):
 #                res=1
 #            fin.append(res)
 # 
 #        return max(fin)
        