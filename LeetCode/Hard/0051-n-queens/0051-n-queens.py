class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset=set()
        posdia=set()
        negdia=set()
        board=[["."]*n for i in range(n)]
        res=[]

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in colset or (r-c) in posdia or (r+c) in negdia:
                    continue
                colset.add(c)
                posdia.add((r-c))
                negdia.add((r+c))
                board[r][c]="Q"

                backtrack(r+1)
                colset.remove(c)
                posdia.remove((r-c))
                negdia.remove((r+c))
                board[r][c]="."

        backtrack(0)
        return res

