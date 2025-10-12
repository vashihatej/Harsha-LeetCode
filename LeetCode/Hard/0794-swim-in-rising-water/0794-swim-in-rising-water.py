import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # The grid is an n x n matrix where grid[r][c] = elevation/time
        # You start at (0,0) and can move in 4 directions (up/down/left/right)
        # You can only swim into a cell when your current time >= its elevation
        # Goal: reach (n-1, n-1) with the minimum time possible
        
        n = len(grid)  # grid size
        
        # 'visit' keeps track of visited cells to avoid processing them twice
        visit = set()
        visit.add((0, 0))
        
        # Min-heap to always explore the lowest-elevation path first
        # Each entry = [current_time (max height so far), row, col]
        minheap = [[grid[0][0], 0, 0]]
        
        # Directions for moving up, down, left, right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while minheap:
            # Pop the cell with the smallest current time (lowest height so far)
            h, r, c = heapq.heappop(minheap)
            
            # If we reached the bottom-right cell, return the time
            if r == n - 1 and c == n - 1:
                return h
            
            # Explore all 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # new row, new col
                
                # Skip out-of-bounds or already visited cells
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visit:
                    continue
                
                visit.add((nr, nc))  # mark new cell as visited
                #add the neigbours to minheap
                heapq.heappush(minheap, [max(h, grid[nr][nc]), nr, nc])
