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
#         """
#         Given a list of travel times 'times', where each entry is (u, v, w),
#         meaning there is a directed edge from node u → v taking time w.

#         n = number of nodes (labeled 1 through n)
#         k = starting node (where the signal starts)

#         Goal: Find the minimum time it takes for all nodes to receive the signal.
#         If any node cannot be reached, return -1.
#         """

#         # ---------------------------
#         # Step 1️⃣: Build adjacency list (graph)
#         # ---------------------------
#         # Example: times = [[2,1,1],[2,3,1],[3,4,1]]
#         # edges = {
#         #   1: [],
#         #   2: [(1,1), (3,1)],
#         #   3: [(4,1)],
#         #   4: []
#         # }
#         edges = {i: [] for i in range(1, n + 1)}
#         for u, v, w in times:
#             edges[u].append((v, w))  # store destination and weight

#         # ---------------------------
#         # Step 2️⃣: Initialize the min-heap (priority queue)
#         # ---------------------------
#         # The heap stores pairs of (time_so_far, current_node)
#         # Start from the source node k with initial time 0
#         min_heap = [(0, k)]

#         # 'visit' keeps track of nodes whose shortest time is already finalized
#         visit = set()

#         # 't' will store the maximum time taken among all reached nodes
#         t = 0

#         # ---------------------------
#         # Step 3️⃣: Dijkstra’s Algorithm using a Min-Heap
#         # ---------------------------
#         # Keep picking the next node with the smallest known signal time
#         while min_heap:
#             # Pop the node that can be reached earliest
#             time_so_far, node = heapq.heappop(min_heap)

#             # If we’ve already visited this node, skip it
#             if node in visit:
#                 continue

#             # Mark this node as visited — we now know its shortest distance
#             visit.add(node)

#             # Update total time: this is the current farthest reached so far
#             t = time_so_far

#             # Explore all neighbors of this node
#             for neighbor, travel_time in edges[node]:
#                 # Only consider unvisited nodes
#                 if neighbor not in visit:
#                     # Push new possible path into heap
#                     # Total time to reach neighbor = current time + travel time
#                     heapq.heappush(min_heap, (time_so_far + travel_time, neighbor))

#         # ---------------------------
#         # Step 4️⃣: Return the answer
#         # ---------------------------
#         # If we visited all nodes → return total time taken
#         # Otherwise, some nodes were unreachable → return -1
#         return t if len(visit) == n else -1
