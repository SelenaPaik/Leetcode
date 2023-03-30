
# intuition: use set
# 1. for every elements in num
# 2. check if that number is in the set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for n in nums:
            if n in myset:
                return True
            myset.add(n)
        return False

