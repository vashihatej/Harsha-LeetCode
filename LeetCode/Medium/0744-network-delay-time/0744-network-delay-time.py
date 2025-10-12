class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for i in range(1, n+1):
            edges[i]=[]
        for u,v,w in times:
            edges[u].append((v,w))
        minheahp=[(0,k)]
        t=0
        visit=set()
        while minheahp:
            w1, n1= heapq.heappop(minheahp)
            if n1 in visit:
                continue
            visit.add(n1)
            t=w1
            
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheahp, (w1+w2,n2))
        return t if len(visit) == n else -1