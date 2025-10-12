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



# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # -----------------------------------------------
#         # Step 1: Build adjacency list (graph representation)
#         # -----------------------------------------------
#         # 'edges' will map each node -> list of (neighbor, time)
#         # Example: if times = [[2,1,1],[2,3,1],[3,4,1]]
#         # edges = {1: [], 2: [(1,1), (3,1)], 3: [(4,1)], 4: []}
#         edges = {}
#         for i in range(1, n + 1):
#             edges[i] = []
        
#         for u, v, w in times:
#             edges[u].append((v, w))   # directed edge from u -> v with weight w

#         # -----------------------------------------------
#         # Step 2: Initialize min-heap (priority queue)
#         # -----------------------------------------------
#         # Each heap entry = (time so far, current node)
#         # We start with the source node 'k' and time 0
#         minheap = [(0, k)]
        
#         # 'visit' will store nodes we already finalized (shortest time found)
#         visit = set()

#         # 't' will track the total time when the last node receives the signal
#         t = 0

#         # -----------------------------------------------
#         # Step 3: Dijkstra’s algorithm using a min-heap
#         # -----------------------------------------------
#         while minheap:
#             # Pop the node with the smallest current time
#             w1, n1 = heapq.heappop(minheap)

#             # If we already visited this node, skip it
#             if n1 in visit:
#                 continue

#             # Mark this node as visited (we now know its shortest signal time)
#             visit.add(n1)

#             # Update 't' to the time it took to reach this node
#             t = w1

#             # -----------------------------------------------
#             # Step 4: Explore all the neighbors of current node
#             # -----------------------------------------------
#             # Each neighbor has a travel time (w2)
#             # We only push it to the heap if it hasn’t been visited
#             for n2, w2 in edges[n1]:
#                 if n2 not in visit:
#                     # Push new pair: (total time to reach n2, node n2)
#                     heapq.heappush(minheap, (w1 + w2, n2))

#         # -----------------------------------------------
#         # Step 5: Return result
#         # -----------------------------------------------
#         # If we visited all nodes, 't' will contain the total time
#         # Else, return -1 (not all nodes were reachable)
#         return t if len(visit) == n else -1
