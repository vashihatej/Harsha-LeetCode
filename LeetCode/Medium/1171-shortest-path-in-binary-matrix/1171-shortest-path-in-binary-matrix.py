class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1
        row, col=len(grid), len(grid[0])
        visit= set()
        queue=deque()
        queue.append((0,0))
        visit.add((0,0))

        l = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r==row-1 and c==col-1 and grid[r][c]==0):
                    return l
                direction = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,1], [-1,-1], [1,-1]]
 
                for ro, co in direction:
                    if min((ro+r), (co+c)) < 0 or ro+r == row or co+c == col or grid[ro+r][co+c] == 1 or (ro+r, co+c) in visit :
                        continue
                    queue.append((ro+r, co+c))
                    visit.add((ro+r, co+c))
            l += 1
        return -1




