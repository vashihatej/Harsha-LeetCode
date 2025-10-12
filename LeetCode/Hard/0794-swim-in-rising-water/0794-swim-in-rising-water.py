import heapq  # for min-heap (priority queue)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Problem:
        You are given an n x n grid where grid[r][c] represents the height
        (or time) required before you can swim into that cell.
        You start at (0,0) and want to reach (n-1, n-1) in minimum time.

        Approach:
        Use a modified Dijkstra’s algorithm.
        Each step picks the cell with the smallest "current time" (water level)
        we can swim to, and we always expand from there.
        """

        n = len(grid)  # grid size

        # Each heap entry = [time_so_far (max height so far), row, col]
        # We start at (0, 0) and the initial time is grid[0][0]
        minheap = [[grid[0][0], 0, 0]]

        # Visited set to avoid re-processing the same cell
        visit = set()
        visit.add((0, 0))

        # Directions for moving in 4 possible ways (down, up, right, left)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minheap:
            # Pop the cell that can be reached with the smallest "current time"
            time, r, c = heapq.heappop(minheap)

            # Base case: if we've reached the destination, return the time
            if r == n - 1 and c == n - 1:
                return time

            # Explore all 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # neighbor row, col

                # Skip if the neighbor is out of bounds or already visited
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visit:
                    continue

                # Mark this neighbor as visited
                visit.add((nr, nc))

                # ---------------------------------------------------------
                # Here’s the KEY difference from normal Dijkstra:
                # In Network Delay, we did:
                #   new_time = cur_time + edge_weight
                # But here, the "cost" is determined by the HIGHEST elevation
                # we've seen so far along the path.
                #
                # So we take the maximum of:
                #   - current time so far (water level)
                #   - height of the neighbor cell (grid[nr][nc])
                # ---------------------------------------------------------
                new_time = max(time, grid[nr][nc])

                # Push the new state into the heap
                heapq.heappush(minheap, [new_time, nr, nc])
