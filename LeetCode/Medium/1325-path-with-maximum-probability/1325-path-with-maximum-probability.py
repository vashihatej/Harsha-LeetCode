class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj={}
        for i in range(n):
            adj[i]=[]
        for i in range(len(edges)):
            src,dest=edges[i]
            adj[src].append((dest,succProb[i]))
            adj[dest].append((src,succProb[i]))
        visit=set()
        maxheap=[(-1,start_node)]
        while maxheap:
            p, end = heapq.heappop(maxheap)
            visit.add(end)
            if end == end_node:
                return -1*p
            for nei, prob in adj[end]:
                if nei not in visit:
                    heapq.heappush(maxheap, (p*prob,nei))
        return 0.0