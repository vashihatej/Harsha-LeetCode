class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Total sum of all stones
        stoneSum = sum(stones)

        # The ideal goal is to make two subsets as close as possible
        # Target = half of the total sum (ceil)
        target = (stoneSum + 1) // 2

        # Memoization dictionary for (i, total)
        dp = {}

        def dfs(i, total):
            """
            i      -> current stone index
            total  -> current sum of one subset (S1)
            returns -> minimum possible final difference |S1 - S2|
            """
            # Base case: if we've processed all stones,
            # or we've already reached/exceeded half the total
            if total >= target or i == len(stones):
                # Compute remaining subset sum as (stoneSum - total)
                # and return absolute difference between the two subsets
                return abs(total - (stoneSum - total))

            # Return cached result if already computed
            if (i, total) in dp:
                return dp[(i, total)]

            # \U0001f539 Option 1: Skip current stone
            skip = dfs(i + 1, total)

            # \U0001f539 Option 2: Include current stone (add to S1)
            include = dfs(i + 1, total + stones[i])

            # Store the best (minimum difference) between both choices
            dp[(i, total)] = min(skip, include)
            return dp[(i, total)]

        # Start recursion from index 0 with sum 0
        return dfs(0, 0)
