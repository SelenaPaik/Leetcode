
# append array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            new  = nums
            nums = nums + new
            return nums