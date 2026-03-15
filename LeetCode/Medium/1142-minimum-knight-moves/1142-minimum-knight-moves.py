from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        We solve this using BFS because we want the MINIMUM number of moves.

        Why BFS?
        -------
        BFS explores positions level-by-level:

            Level 0 → starting position
            Level 1 → all squares reachable in 1 move
            Level 2 → all squares reachable in 2 moves
            ...

        The first time we reach the target (x, y), we are guaranteed
        that it is the minimum number of moves.

        ------------------------------------------------------------

        Important Observation (Symmetry)
        --------------------------------
        The chess board is infinite and knight movement is symmetric.

        For example:
            Distance to (5,5)  == Distance to (-5,5)
            Distance to (5,5)  == Distance to (5,-5)
            Distance to (5,5)  == Distance to (-5,-5)

        Because knight moves can mirror across axes.

        Therefore we convert the target to positive coordinates:

            x = abs(x)
            y = abs(y)

        This allows us to search only in the first quadrant
        and greatly reduces the search space.

        ------------------------------------------------------------

        Knight Moves
        ------------

        A knight always moves in an L-shape:

            2 squares in one direction
            1 square in the perpendicular direction

        Possible moves from (cx, cy):

            (cx+2, cy+1)
            (cx+2, cy-1)
            (cx-2, cy+1)
            (cx-2, cy-1)
            (cx+1, cy+2)
            (cx+1, cy-2)
            (cx-1, cy+2)
            (cx-1, cy-2)

        So each square can generate 8 next states.

        ------------------------------------------------------------

        Why do we restrict exploration to nx >= -2 and ny >= -2 ?
        ----------------------------------------------------------

        The board is infinite. Without any restriction,
        BFS could explore positions like:

            (-100, -200)
            (-50, 300)
            (-500, -10)

        which are extremely far from the target and
        will never be part of the optimal path.

        However we cannot completely forbid negative coordinates,
        because sometimes the optimal knight path temporarily
        moves slightly into negative space.

        Example:
            target = (1,1)

        shortest path:

            (0,0)
              ↓
            (-1,2)
              ↓
            (1,1)

        Notice we visited (-1,2), which is negative in x.

        Therefore we allow a small negative boundary.

        Empirically it is safe to limit exploration to:

            nx >= -2
            ny >= -2

        because an optimal knight path will never need to go
        further negative than -2 to reach a positive target.

        This pruning dramatically reduces the BFS search space
        while still guaranteeing correctness.

        ------------------------------------------------------------

        Data Structures
        ---------------

        queue   → BFS frontier storing (x, y, steps)
        visited → prevents revisiting the same position

        """

        # Convert target to first quadrant due to symmetry
        x = abs(x)
        y = abs(y)

        # All 8 possible knight moves
        directions = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]

        # BFS queue stores (current_x, current_y, steps_taken)
        queue = deque([(0,0,0)])

        # Track visited positions to avoid infinite loops
        visited = set([(0,0)])

        while queue:

            cx, cy, steps = queue.popleft()

            # If we reach the target position, return steps
            if (cx, cy) == (x, y):
                return steps

            # Explore all possible knight moves
            for dx, dy in directions:

                nx = cx + dx
                ny = cy + dy

                """
                Pruning conditions:

                1) Avoid revisiting positions we've already explored
                   because BFS guarantees the first visit is shortest.

                2) Restrict exploration so BFS does not wander
                   too far into useless negative coordinates.

                nx >= -2 and ny >= -2 keeps search near the region
                where the optimal path exists.
                """

                if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))