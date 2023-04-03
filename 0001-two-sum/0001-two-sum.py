# intuition : subtract value from target, and find that result from array
# 
# 1.brute force
# 



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans =[]
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    ans.append(i)
                    ans.append(j)
        return ans