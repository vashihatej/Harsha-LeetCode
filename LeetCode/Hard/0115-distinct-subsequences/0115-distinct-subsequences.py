class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Memoization dictionary
        # Key: (s1, s2)  →  number of subsequences starting from these indices
        dp = {}

        def dfs(s1, s2):
            """
            Returns the number of distinct subsequences of s[s1:]
            that form t[s2:].
            """

            # \U0001f3af Base Case 1: We've formed all of t successfully
            # Example: s = "abc", t = "ab"  → once s2 == len(t), that’s one valid subsequence
            if s2 == len(t):
                return 1

            # \U0001f9f1 Base Case 2: We've run out of characters in s but still have more t left
            # No way to complete t now.
            if s1 == len(s):
                return 0

            # \U0001f9e0 If already computed → return memoized result
            if (s1, s2) in dp:
                return dp[(s1, s2)]

            # \U0001f680 Case 1: Characters match → two options
            if s[s1] == t[s2]:
                # Option 1️⃣: Use s[s1] to match t[s2] → move both pointers
                # Option 2️⃣: Skip s[s1] and look for other matches later → move s1 only
                dp[(s1, s2)] = dfs(s1 + 1, s2 + 1) + dfs(s1 + 1, s2)
            else:
                # \U0001f6ab Characters don't match → we can only skip s[s1]
                dp[(s1, s2)] = dfs(s1 + 1, s2)

            # \U0001f4dd Store and return result
            return dp[(s1, s2)]

        # Start recursion from the beginning of both strings
        return dfs(0, 0)
