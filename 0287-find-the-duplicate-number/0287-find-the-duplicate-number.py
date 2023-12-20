# dictionary size = n = len(nums)-1 
# (int, bool)
# 1. Initialize all elements to False
# 2. If element exist, put True
# 3. If element already checked(True), return that element

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check={}
        for i in range(len(nums)):
            check[i+1]=False
            
        for num in nums:
            if check[num]==True:
                return num
            else:
                check[num] = True
            