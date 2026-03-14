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
    def numberOfPaths(self, grid, k):
        """
        Top-down DFS with memoization.

        State:
            (i, j, remainder)

        Meaning:
            number of valid paths from cell (i,j) to bottom-right
            where the current path sum % k = remainder
        """

        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        # memo[i][j][r] stores computed results
        memo = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def dfs(i, j, remainder):

            # If outside grid → invalid path
            if i >= m or j >= n:
                return 0

            # update remainder including current cell
            remainder = (remainder + grid[i][j]) % k

            # reached destination
            if i == m - 1 and j == n - 1:
                return 1 if remainder == 0 else 0

            # return memoized result if already computed
            if memo[i][j][remainder] != -1:
                return memo[i][j][remainder]

            # explore both directions
            down = dfs(i + 1, j, remainder)
            right = dfs(i, j + 1, remainder)

            memo[i][j][remainder] = (down + right) % MOD

            return memo[i][j][remainder]

        return dfs(0, 0, 0)