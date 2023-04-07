
# l,r = 0, len(height)-1
# if height[r] < height[l]: 
#     r-=1
# else:
#     l+=1
#     
# calculate the area = min(height[r],height[l]) * (r-l)
# keep the track of max

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxval = 0
        while l<r:
            area = min(height[r], height[l]) * (r-l)
            if maxval < area:
                maxval = area
            if height[r] < height[l] :
                r-=1
            else:
                l+=1
        return maxval
            