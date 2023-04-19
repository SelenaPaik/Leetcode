
# do binary search for every row
# for each row, set l,r 
# check if matrix[row][r] < target -> if so, move to next row
# if not, do binary search within that row

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        def binary(arr:List[int], target:int) -> bool:
            l,r = 0, len(arr)-1
            print(arr, target)
            while(l<=r):
                mid =  math.floor((l+r)/2)
                if arr[mid]==target:
                    return True
                if arr[mid] < target:
                    l= mid+1
                if arr[mid] > target:
                    r = mid-1
            return False
        
        for row in range(len(matrix)):
            l,r = 0, len(matrix[row])-1
            if matrix[row][r] >= target:
                res =binary(matrix[row], target)
                break
        return res