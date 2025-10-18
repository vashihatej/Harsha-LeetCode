class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Memoization dictionary: key = (i, m, n)
        dp = {}

        # Precompute number of 0s and 1s in each string for efficiency
        counts = []
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            counts.append((zeros, ones))

        def dfs(i, m_left, n_left):
            """
            i       -> current index in strs
            m_left  -> remaining 0s we can still use
            n_left  -> remaining 1s we can still use
            returns -> max number of strings we can include from i onwards
            """
            # Base case: reached the end of list
            if i == len(strs):
                return 0

            # Check cache
            if (i, m_left, n_left) in dp:
                return dp[(i, m_left, n_left)]

            zeros, ones = counts[i]

            # Option 1: Skip this string
            skip = dfs(i + 1, m_left, n_left)

            # Option 2: Include this string (only if fits within limits)
            include = 0
            if m_left >= zeros and n_left >= ones:
                include = 1 + dfs(i + 1, m_left - zeros, n_left - ones)

            # Store best result
            dp[(i, m_left, n_left)] = max(skip, include)
            return dp[(i, m_left, n_left)]

        # Start recursion from index 0 with full m and n
        return dfs(0, m, n)
