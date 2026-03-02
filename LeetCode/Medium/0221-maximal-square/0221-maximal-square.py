class Solution:
    def maximalSquare(self, matrix):
        """
        TOP-DOWN DP (Recursion + Memoization)

        For each cell (r, c):
        We calculate the largest square that STARTS at (r, c).

        If matrix[r][c] == "1":
            square_size = 1 + min(
                square starting at right,
                square starting at down,
                square starting at diagonal
            )
        Else:
            square_size = 0
        """

        if not matrix:
            return 0

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # cache[(r,c)] = side length of largest square starting at (r,c)
        cache = {}

        def helper(r, c):

            # If outside matrix → no square
            if r >= ROWS or c >= COLS:
                return 0

            # If already computed → return cached value
            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = 0

            # Only try to grow square if current cell is "1"
            if matrix[r][c] == "1":

                down  = helper(r + 1, c)
                right = helper(r, c + 1)
                diag  = helper(r + 1, c + 1)

                # Square grows based on smallest neighbor
                cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        # IMPORTANT:
        # We must call helper on ALL cells,
        # because largest square might start anywhere.
        for r in range(ROWS):
            for c in range(COLS):
                helper(r, c)

        # cache now contains square size for every cell
        # We take the maximum side length and square it (area)
        return max(cache.values()) ** 2

        """
        =========================
        EXAMPLE WALKTHROUGH
        =========================

        Example matrix:

        [
         ["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]
        ]

        Our goal:
        Find the largest square consisting only of "1"s.

        ----------------------------------------------------
        HOW THIS RECURSIVE APPROACH WORKS
        ----------------------------------------------------

        For every cell (r, c), we ask:

            "If I start a square from here,
             how big can that square become?"

        helper(r, c) returns:
            The SIDE LENGTH of the largest square
            that STARTS at position (r, c).

        ----------------------------------------------------
        WHY DO WE CHECK DOWN, RIGHT, AND DIAGONAL?
        ----------------------------------------------------

        A square starting at (r, c) looks like this:

            (r,c)      (r,c+1)
            (r+1,c)    (r+1,c+1)

        To grow a square from (r,c):

        - The cell below (down) must support a square
        - The cell to the right must support a square
        - The diagonal must support a square

        If ANY of those is smaller,
        the square cannot grow beyond that size.

        Therefore:

            square_size =
                1 + min(
                    down,
                    right,
                    diagonal
                )

        The MIN is taken because
        the smallest neighbor limits growth.

        ----------------------------------------------------
        STEP-BY-STEP VISUAL RESULT
        ----------------------------------------------------

        After computing helper(r,c) for all cells,
        the conceptual DP (side lengths) becomes:

            2 0 1 0 0
            1 0 2 2 1
            1 1 1 1 1
            1 0 0 1 0

        Explanation of one important cell:

        Consider cell (1,2) which is "1":

            matrix region:
                1 1
                1 1

        Neighbors:
            down  = helper(2,2) = 1
            right = helper(1,3) = 1
            diag  = helper(2,3) = 1

        So:

            helper(1,2) = 1 + min(1,1,1)
                         = 2

        That means:
            Largest square starting at (1,2)
            has side length 2.

        ----------------------------------------------------
        FINAL STEP
        ----------------------------------------------------

        We compute helper(r,c) for ALL cells
        because the largest square
        might start anywhere in the matrix.

        Then:

            max_side = maximum value in cache
            answer   = max_side * max_side

        Because:
            Problem asks for AREA,
            not side length.

        In this example:

            max_side = 2
            area = 2 * 2 = 4

        ----------------------------------------------------
        KEY INTUITION
        ----------------------------------------------------

        Each cell asks:
            "Can I be the top-left corner
             of a bigger square?"

        It can grow only if:
            - I am "1"
            - Right supports growth
            - Down supports growth
            - Diagonal supports growth

        The smallest neighbor determines
        how big the square can be.
        """