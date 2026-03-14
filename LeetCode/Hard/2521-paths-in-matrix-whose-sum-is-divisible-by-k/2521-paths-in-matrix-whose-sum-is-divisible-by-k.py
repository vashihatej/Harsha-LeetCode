# class Solution:
#     def numberOfPaths(self, grid, k):
#         """
#         DFS solution (no DP).

#         We explore all possible paths from (0,0) to (m-1,n-1)
#         moving only right or down.

#         Instead of tracking the full sum, we track:
#             sum % k

#         because the problem only cares whether the final sum
#         is divisible by k.

#         This reduces the value range we carry during recursion.
#         """

#         m = len(grid)
#         n = len(grid[0])

#         self.paths = 0

#         def dfs(i, j, cur_sum):
#             """
#             i, j      -> current cell
#             cur_sum -> current path sum
#             """

#             # If outside grid stop exploring
#             if i >= m or j >= n:
#                 return

#             # Update cur_sum including current cell value
#             cur_sum = cur_sum+grid[i][j]

#             # If we reached bottom-right cell
#             if i == m - 1 and j == n - 1:

#                 # Check if path sum is divisible by k
#                 if cur_sum%k == 0:
#                     self.paths +=1
#                 return

#             # Move DOWN
#             dfs(i + 1, j, cur_sum)

#             # Move RIGHT
#             dfs(i, j + 1, cur_sum)

#         # Start DFS from (0,0)
#         dfs(0, 0, 0)

#         return self.paths

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        """
        Problem
        -------
        We start at the top-left cell (0,0) of a matrix and want to reach
        the bottom-right cell (ROWS-1,COLS-1). From each cell we can move:

            1) RIGHT  -> (r, c+1)
            2) DOWN   -> (r+1, c)

        For every path we calculate the sum of values along the path.
        A path is valid only if:

            path_sum % k == 0

        -------------------------------------------------------------

        Key Observation
        ---------------
        Instead of storing the full path sum, we only need to track:

            remainder = path_sum % k

        because:

            (a + b) % k = ((a % k) + (b % k)) % k

        So two paths that reach the same cell with the same remainder
        will behave identically for the rest of the path.

        Example:
            Path1 sum = 11 -> 11 % 3 = 2
            Path2 sum = 14 -> 14 % 3 = 2

        From that point onward the future possibilities are identical.

        Therefore our state becomes:

            (row, col, remainder)

        -------------------------------------------------------------

        DFS State
        ---------
        dfs(r, c, remainder) returns:

            number of valid paths from cell (r,c)
            to the bottom-right corner where the
            current path sum % k = remainder.

        -------------------------------------------------------------

        Memoization
        -----------
        We store results of previously computed states:

            cache[r][c][remainder]

        This prevents recomputing the same state many times.

        Without memoization the recursion tree grows exponentially.
        With memoization we compute each state only once.

        -------------------------------------------------------------

        Complexity
        ----------
        Number of states = ROWS * COLS * k

        Maximum constraints:
            ROWS ≤ 50
            COLS ≤ 50
            k ≤ 50

        So total states ≤ 125000

        Time Complexity  = O(ROWS * COLS * k)
        Space Complexity = O(ROWS * COLS * k)

        -------------------------------------------------------------

        Why MOD = 10^9 + 7
        -------------------
        The number of possible paths can become extremely large.
        To avoid integer overflow and to keep numbers manageable,
        we return the answer modulo:

            10^9 + 7

        This is a large prime commonly used in programming problems.
        """

        ROWS, COLS = len(grid), len(grid[0])

        # cache[r][c][remain] stores number of valid paths from (r,c)
        # when current path sum % k == remain
        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]

        MOD = 10**9 + 7

        def dfs(r, c, remain):

            # If we reached bottom-right cell
            if r == ROWS - 1 and c == COLS - 1:
                remain = (remain + grid[r][c]) % k
                return 1 if remain == 0 else 0

            # If outside grid -> invalid path
            if r == ROWS or c == COLS:
                return 0

            # If already computed, return cached result
            if cache[r][c][remain] != -1:
                return cache[r][c][remain]

            # Update remainder after including current cell
            new_rem = (remain + grid[r][c]) % k

            # Explore two possible moves
            down_paths = dfs(r + 1, c, new_rem)
            right_paths = dfs(r, c + 1, new_rem)

            # Store result in cache
            cache[r][c][remain] = (down_paths + right_paths) % MOD

            return cache[r][c][remain]

        # Start DFS from top-left with remainder 0
        return dfs(0, 0, 0)