
# intuition: check duplicates in columns, rows, and sub-boxes
# if there's duplicate, return False
# 
# for each column, row, box
# make dictionary for 1-9
# +1 when we find a number
# if value >= 2, return False
# 
def checksquare(x:int, y:int, board: List[List[str]]) -> bool:
        numdic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        ans = True
        for i in range(0,3):
            for j in range(0,3):
                #print(x+i,y+j)
                if board[i+x][y+j] != ".":
                    numdic[board[x+i][y+j]] += 1
                    if numdic[board[x+i][y+j]] >= 2:
                        print("square False")
                        ans = False
                        return False
        return ans
class Solution:
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        
        for i in range(0, len(board)):
            numdic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for j in range(0,9):
                if board[i][j] != ".":
                    numdic[board[i][j]] += 1
                    if numdic[board[i][j]] >= 2:
                        return False
                        
        
        for i in range(0,9):
            numdic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for j in range(0,9):
                if board[j][i] != ".":
                    numdic[board[j][i]] += 1
                    print(board[j][i], numdic[board[j][i]])
                    if numdic[board[j][i]] >= 2:
                        print("col False")
                        return False
                
        
        for i in range(0,3):
            for j in range(0,3):
                ans = checksquare(3*i,3*j, board)
                if ans == False:
                    return False
       
        return ans
        
                