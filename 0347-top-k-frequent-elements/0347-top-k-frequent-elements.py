# intuition: use dictionary(number - count)
#     
# 1. put number(key) and count(value) to dictionary
# 2. sort it with count(value)
# 3. print keys with top k values


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans =[]
        for n in nums:
            dic[n] = 0
        for n in nums:
            dic[n] += 1
            
        sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse = True)
        count = 0
        
        for key in sorted_dic:
            if count<k:
                ans.append(key[0])
                count += 1
        return ans