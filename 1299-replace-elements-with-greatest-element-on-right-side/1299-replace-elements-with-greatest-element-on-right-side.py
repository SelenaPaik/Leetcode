
# intuition: make a new array, and append the greatest value 
# 
# start from the last element(to find out the greatest value)
# put -1 in the last element
# 
# 1. start from the last element, find max value
# 2. for each element, put max value in the front of new array



class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        ans = []
        for i in range(len(arr)-1, 0,-1):
            if max < arr[i] :
                max = arr[i]
            ans.insert(0, max)
            
        # put -1 in the last (append)    
        ans.append(-1)
        
        return ans