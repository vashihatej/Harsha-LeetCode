class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS= len(matrix), len(matrix[0])
        cache={}
        def helper(r,c):
            if r >= ROWS or c>= COLS:
                return 0
            if (r,c) not in cache:
                right=helper(r,c+1)
                bottom=helper(r+1,c)
                botrig=helper(r+1,c+1)
                cache[(r,c)]=0
                if matrix[r][c]=="1":
                    cache[(r,c)]=1+min(right, bottom, botrig)
            return cache[(r,c)]
        helper(0,0)
        return max(cache.values())**2