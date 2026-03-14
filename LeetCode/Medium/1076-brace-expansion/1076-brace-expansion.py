
class Solution:
    def expand(self, s):
        """
        PROBLEM
        -------
        The string may contain letters or groups like {a,b,c}.
        Each position represents multiple possible characters.

        Example:
            "{a,b}c{d,e}f"

        becomes

            [
              ['a','b'],
              ['c'],
              ['d','e'],
              ['f']
            ]

        Our task:
        Generate all possible combinations by picking one
        character from each position.

        This is a classic BACKTRACKING problem.

        ------------------------------------------------

        APPROACH
        --------

        Step 1: Parse the string into character options.

        Step 2: Use DFS / Backtracking to build words.

        At each step we:
            choose a letter
            move to next position
            backtrack

        ------------------------------------------------

        Example recursion tree:

                    ""
               /        \
              a          b
              |          |
              c          c
            /   \      /   \
           d     e    d     e
           |     |    |     |
           f     f    f     f

        Result:
            acdf
            acef
            bcdf
            bcef
        """

        groups = []
        i = 0

        # -----------------------
        # Step 1: Parse the string
        # -----------------------
        while i < len(s):

            if s[i] == '{':
                i += 1
                chars = []

                # collect all characters inside braces
                while s[i] != '}':
                    if s[i] != ',':
                        chars.append(s[i])
                    i += 1

                groups.append(sorted(chars))

            else:
                # single character option
                groups.append([s[i]])

            i += 1

        # -----------------------
        # Step 2: Backtracking
        # -----------------------

        result = []

        def dfs(index, path):
            """
            index → which group we are choosing from
            path  → current word being built
            """

            # If we picked characters for all positions
            if index == len(groups):
                result.append("".join(path))
                return

            # Try all characters in this group
            for ch in groups[index]:
                path.append(ch)
                dfs(index + 1, path)
                path.pop()  # backtrack

        dfs(0, [])

        return result