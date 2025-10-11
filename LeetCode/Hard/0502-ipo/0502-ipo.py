import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # maxheap: to select the project with the highest profit among affordable ones
        maxheap = []

        # minheap: store all projects by their required capital
        # Each entry = (required_capital, profit)
        # So the smallest capital requirement is always at the top
        minheap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minheap)  # O(n log n) → builds heap efficiently

        # We can do at most k projects
        for _ in range(k):

            # Move all projects we can afford (capital ≤ current w) into maxheap
            while minheap and minheap[0][0] <= w:
                c, p = heapq.heappop(minheap)   # remove from minheap
                heapq.heappush(maxheap, -1 * p)     # push profit as negative to make max-heap

            # If we can't afford any project, stop early
            if not maxheap:
                break

            # Pick the most profitable available project
            w += -1 * heapq.heappop(maxheap)

        # Return the maximized capital after at most k projects
        return w
