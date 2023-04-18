# count the number of parenthesis
# opencnt, closecnt
# we can add parenthesis only when cnt < n
# open: add when open<n
# close: add when closed<open
# if len(current parenthesis)==n : add string to array

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

        
        