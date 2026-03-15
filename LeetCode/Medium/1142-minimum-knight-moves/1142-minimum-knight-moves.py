from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        We solve this using BFS because we want the minimum number of moves.

        BFS explores the board level-by-level:
        Level 0 -> starting position
        Level 1 -> all squares reachable in 1 move
        Level 2 -> squares reachable in 2 moves
        etc.

        The first time we reach (x,y) we are guaranteed to have the minimum moves.
        """

        # Because the board is symmetric, we only need to work with positive coordinates
        x = abs(x)
        y = abs(y)

        # All possible knight moves
        directions = [
            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)
        ]

        # BFS queue: (current_x, current_y, steps)
        queue = deque([(0,0,0)])

        # Track visited positions
        visited = set([(0,0)])

        while queue:

            cx, cy, steps = queue.popleft()

            # If we reach target, return steps
            if (cx,cy) == (x,y):
                return steps

            # Explore all possible knight moves
            for dx, dy in directions:

                nx = cx + dx
                ny = cy + dy

                # Avoid exploring too far into negative space
                # small pruning optimization
                if (nx,ny) not in visited:

                    visited.add((nx,ny))
                    queue.append((nx,ny,steps+1))