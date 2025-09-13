class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # ROWS, COL = len(grid), len(grid[0])
        # q = deque()
        # time, fresh = 0, 0

        # for r in range(ROWS):
        #     for c in range(COL):
        #         if grid[r][c] == 1:      #get the total number of fresh oranges so that in the end we can tll all the oreanges were rotten or we have any fresh ones to return -1
        #             fresh+=1
        #         if grid[r][c] ==2:       #append all rotten oranges initially so that you can start BFS from those oranges
        #             q.append([r, c])

        # while q and fresh > 0:

        #     for i in range(len(q)):
        #         r, c = q.popleft()
        #         direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #         for dr, dc in direction:
        #             row, col = dr+r, dc+c
        #             if(row < 0 or row == len(grid) or 
        #             col < 0 or col == len(grid[0]) or 
        #             grid[row][col] != 1):                    #if the orange is not fresh then continue 
        #                 continue
        #             q.append([row, col])                     #when there is a fresh orange adjacent append that to queue so that its neighbour oranges will be marked rotten in next time interval
        #             grid[row][col] == 2              #marking the current orange as rotten
        #             fresh -= 1
        #     time += 1                                 #at each level of BFS increament the time taken
        # return time if fresh == 0 else -1             #return time if there are no fresh oranges left

        row, col=len(grid), len(grid[0])
        visit = set()
        queue= deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh +=1
                elif grid[r][c]==2:
                    queue.append((r,c))
                    visit.add((r,c))
        l=0
        while queue and fresh >0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                direction = [[1,0], [-1,0], [0,1], [0,-1]]
 
                for ro, co in direction:
                    if min((ro+r), (co+c)) < 0 or ro+r == row or co+c == col or grid[ro+r][co+c] != 1 or (ro+r, co+c) in visit :
                        continue
                    fresh -=1
                    grid[r][c]==2
                    queue.append((ro+r, co+c))
                    visit.add((ro+r, co+c))
            l += 1
        return l if fresh == 0 else -1


