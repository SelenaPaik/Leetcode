# use pointer
# binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        mid = math.floor((r+l)/2)
        while(l<=r):
            if nums[mid] < target:
                l = mid+1
                mid = math.floor((r+l)/2)
            if nums[mid] > target:
                r = mid-1
                mid = math.floor((r+l)/2)
            
            if nums[mid]==target:
                return mid
        return -1
        
      