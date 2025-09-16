class NumMatrix:
    """
    2D Range Sum (Immutable) using a 2D prefix sum table.

    Idea:
      - Precompute a table P where P[r][c] = sum of matrix[0..r][0..c].
      - Then any sub-rectangle sum can be answered in O(1) using inclusion–exclusion:
            sum(row1..row2, col1..col2)
          = P[row2][col2]
            - (area above the rectangle)        -> P[row1-1][col2]        if row1 > 0
            - (area left  of the rectangle)     -> P[row2][col1-1]        if col1 > 0
            + (overlap of above & left areas)   -> P[row1-1][col1-1]      if row1 > 0 and col1 > 0
    """

    def __init__(self, matrix: list[list[int]]):
        # Handle an empty matrix defensively (LeetCode constrains m,n>=1, but this keeps it robust)
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.m = m
        self.n = n

        # P[r][c] will hold the sum of the rectangle from (0,0) to (r,c), inclusive.
        self.P = [[0] * n for _ in range(m)]

        # Build the prefix table row by row.
        # We keep a running sum 'row_sum' for the current row to avoid re-summing left cells.
        for r in range(m):
            row_sum = 0  # sum of matrix[r][0..c]
            for c in range(n):
                row_sum += matrix[r][c]                 # add current cell into current row's running sum
                above = self.P[r - 1][c] if r > 0 else 0  # sum of everything directly above this cell
                # Total up to (r,c) = (sum of this row up to c) + (sum of all rows above)
                self.P[r][c] = row_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Return the sum of matrix elements in the rectangle with corners:
          top-left     = (row1, col1)
          bottom-right = (row2, col2)
        All indices are 0-based and inclusive.
        """

        # Start with the total sum of the big rectangle (0,0) -> (row2,col2).
        total = self.P[row2][col2]

        # Subtract the area *above* the target rectangle if there is any (rows 0..row1-1).
        if row1 > 0:
            total -= self.P[row1 - 1][col2]

        # Subtract the area *left* of the target rectangle if there is any (cols 0..col1-1).
        if col1 > 0:
            total -= self.P[row2][col1 - 1]

        # We've subtracted the top-left overlap twice; add it back once if it exists.
        if row1 > 0 and col1 > 0:
            total += self.P[row1 - 1][col1 - 1]

        return total
