# binary search
# if nums[l] < nums[r]: return nums[l]
# nums[l] will always bigger than nums[r] if rotated
# compare nums[mid] to nums[l] 
# if nums[l]> nums[mid]: 
#     min is between l~mid
#     r = mid-1
# else: 
#     min is between mid~r 
#     l = mid+1
# update res

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        mid = int((l+r)/2)
        res = nums[mid]
        
        if nums[l] < nums[r] : return nums[l]
        
        while(l<=r):
            mid = int((l+r)/2)
            if nums[r]<res:
                res = nums[r]
            if nums[l]<res:
                res = nums[l]
            if nums[mid]<res:
                res = nums[mid]
            if nums[l]> nums[mid]: 
                r = mid-1
            else:
                l = mid+1

        return res