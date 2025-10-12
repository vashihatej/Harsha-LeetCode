import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Problem:
        Given a list of points on a 2D plane, connect all points such that
        the total cost (sum of Manhattan distances between connected points)
        is minimum, and the graph remains fully connected.

        Approach:
        Use Prim’s Minimum Spanning Tree (MST) algorithm.

        Steps:
        1. Build a graph where each point can connect to every other point.
           The edge weight = Manhattan distance between the two points.
        2. Use a min-heap to always pick the smallest edge that connects
           a new point to the existing MST.
        3. Keep adding edges until all points are connected.
        """

        n = len(points)

        # --------------------------------------------
        # Step 1️⃣: Build adjacency list (complete graph)
        # --------------------------------------------
        # For each pair of points, compute the Manhattan distance.
        # Distance formula: |x1 - x2| + |y1 - y2|
        adj = {i: [] for i in range(n)}  # adjacency list for all points

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
                # Since the graph is undirected, add both ways
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # --------------------------------------------
        # Step 2️⃣: Prim’s Algorithm Initialization
        # --------------------------------------------
        visit = set()           # keeps track of visited points (MST nodes)
        minheap = [[0, 0]]      # (weight, node) - start from node 0
        total_cost = 0          # final MST total weight

        # --------------------------------------------
        # Step 3️⃣: Build MST using Min-Heap
        # --------------------------------------------
        # Keep adding edges with smallest distance until all nodes are visited
        while len(visit) < n:
            weight, node = heapq.heappop(minheap)  # pick smallest edge

            # Skip if the node is already added to MST
            if node in visit:
                continue

            # Add the node to MST
            visit.add(node)
            total_cost += weight

            # Explore all neighbors of this node
            for nei_w, nei in adj[node]:
                if nei not in visit:
                    # Push all possible edges to the heap
                    # Only edges leading to unvisited nodes are useful
                    heapq.heappush(minheap, [nei_w, nei])

        # --------------------------------------------
        # Step 4️⃣: Return final MST cost
        # --------------------------------------------
        return total_cost
