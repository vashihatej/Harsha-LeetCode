class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Key: (i, j) = current positions in s1 and s2
        # Value: True/False whether s3[i+j:] can be formed from s1[i:] and s2[j:]
        dp = {}

        # \U0001f6ab Quick length check
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j, k):
            """
            Recursive DFS to check if s3[k:] can be formed
            by interleaving s1[i:] and s2[j:].
            """

            # \U0001f3af Base case:
            # We've formed all of s3 successfully.
            # Then both s1 and s2 must also be completely used.
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            # \U0001f9e0 Memoization check
            if (i, j) in dp:
                return dp[(i, j)]

            # Start with False (haven’t found a valid path yet)
            res = False

            # 1️⃣ Try using the next character from s1, if it matches s3[k]
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)

            # 2️⃣ If we still haven't found a valid interleaving (`not res`),
            # try using the next character from s2 instead.
            #
            # ⚡ Why "if not res" matters:
            # - Without it, we'd always explore BOTH branches even if
            #   the first one already succeeded.
            # - Worse, Python would overwrite res:
            #       res = dfs(...)  # from s1 → returns True
            #       res = dfs(...)  # from s2 → returns False
            #   ⇒ overall False (even though a valid path exists)
            #
            #   So we only try the second option if the first path failed.
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            # \U0001f4dd Store the result for this (i, j)
            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)
