class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj={}
        n=len(points)
        for i in range(n):
            adj[i]=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1, n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        visit=set()
        res=0
        minheap=[[0,0]]


        while len(visit)<n:
            w,node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            res+=w
            for wei, nie in adj[node]:
                if nie not in visit:
                    heapq.heappush(minheap, (wei,nie))
        return res

