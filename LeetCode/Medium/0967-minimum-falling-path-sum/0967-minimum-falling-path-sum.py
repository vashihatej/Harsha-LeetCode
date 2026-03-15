class Solution:
    def minFallingPathSum(self, matrix):
        """
        Recursive solution.

        Idea:
        A falling path starts at row 0 and moves down one row at a time.

        From position (r, c) we can move to:
            (r+1, c-1)
            (r+1, c)
            (r+1, c+1)

        We recursively compute the minimum path starting from each cell.

        Base Case:
            If we reach the last row, return that cell value.

        Final Answer:
            Try starting from every column in row 0
            and take the minimum path sum.
        """

        n = len(matrix)
        dp={}

        def dfs(r, c):
            # If column goes out of bounds, this path is invalid
            if c < 0 or c >= n:
                return float("inf")
            if (r,c) in dp:
                return dp[(r,c)]

            # If we reach last row, return its value
            if r == n - 1:
                return matrix[r][c]

            # Recursively compute next moves
            left = dfs(r + 1, c - 1)
            down = dfs(r + 1, c)
            right = dfs(r + 1, c + 1)

            # Current cell value + best of the next options
            dp[(r,c)]=matrix[r][c] + min(left, down, right)
            return dp[(r,c)]

        result = float("inf")

        # Try starting from every column in first row
        for col in range(n):
            result = min(result, dfs(0, col))

        return result