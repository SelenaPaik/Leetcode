#dictionary size = n = len(nums)-1 
#(int, bool)

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
            