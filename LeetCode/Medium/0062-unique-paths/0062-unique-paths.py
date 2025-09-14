class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
        def dp(rows, cols):
            prevRow = [0] * cols

            for r in range(rows - 1, -1, -1):
                curRow = [0] * cols
                curRow[cols - 1] = 1
                for c in range(cols - 2, -1, -1):
                    curRow[c] = curRow[c + 1] + prevRow[c]
                prevRow = curRow
            return prevRow[0]
        return dp(m, n)