class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit=set()
        visit.add((0,0))
        n=len(grid)
        minheap=[[grid[0][0],0,0]]
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        while minheap:
            h,r,c=heapq.heappop(minheap)
            if r ==n-1 and c==n-1:
                return h
            for dr,dc in direction:
                neir = r+dr
                neic= c+dc
                if neir < 0 or neic <0 or neic ==n or neir==n or (neir,neic) in visit:
                    continue
                visit.add((neir,neic))
                heapq.heappush(minheap, [max(h,grid[neir][neic]),neir,neic])
