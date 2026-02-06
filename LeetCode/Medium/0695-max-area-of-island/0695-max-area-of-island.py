class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # rows, col = len(grid), len(grid[0])
        # visit = set()
        # self.max_area1 = 0

        # def bfs(r, c):
        
        #     q = collections.deque() #add all the adjacent nodes to queue
        #     visit.add((r, c)) #we want to use add as because visit is a set
        #     q.append((r, c))  #append the first root or starting node to queue
        #     max_area=1
        #     while q:
        #         ro, co= q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]   #all 4 directions to check for lands means "1"

        #         for dr, dc in directions:    #going in all 4 direc to mark the adjacent land("1") nodes to visited
        #             r, c= ro+dr, co+dc
        #             if(r in range(rows) and c in range(col) and grid[r][c] == 1 and (r, c) not in visit):
        #                 visit.add((r, c))
        #                 q.append((r, c))       #adding adaject nodes in bfs 
        #                 max_area += 1
        #     # return max_area
        #     self.max_area1 = max(self.max_area1, max_area)

        # # area=0
        # for r in range(rows):
        #     for c in range(col):
        #         if grid[r][c] == 1 and (r, c) not in visit: # check if it is a land means "1" and also not   
        #             bfs(r, c)
        #             # area = max(area, bfs(r, c))                #visited then this will be an new island so do bfs to mark 
        #                                                             #all adajacent points as visited and get the area then update the maximum 
        # return self.max_area1



        #Using DFS
        rows, col = len(grid), len(grid[0])
        max_area = 0
        visit=set()


        def dfs(r, c):
            
            if min(r, c) < 0 or r== rows or c==col or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1)+ dfs(r, c-1))

        for r in range(rows):
            for c in range(col):
                if grid[r][c]==1 and (r, c) not in visit:
                    max_area=max(max_area, dfs(r, c))
        return max_area