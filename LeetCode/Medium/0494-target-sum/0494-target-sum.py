class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization dictionary to store computed results
        # Key: (index, current_total)
        # Value: number of ways to reach target from this state
        dp = {}

        # Recursive DFS function
        def dfs(i, total):
            """
            i     -> current index in nums
            total -> current running sum considering +/- signs up to this point
            """

            # \U0001f9e9 Base case:
            # If we've processed all numbers,
            # check if the total equals the target.
            if i == len(nums):
                # If the sum matches target → one valid way
                return 1 if total == target else 0

            # \U0001f501 Check memoized results to avoid recomputation
            if (i, total) in dp:
                return dp[(i, total)]

            # \U0001f9ed Recursive exploration:
            # Option 1 → choose "+" for current number
            add = dfs(i + 1, total + nums[i])

            # Option 2 → choose "-" for current number
            subtract = dfs(i + 1, total - nums[i])

            # \U0001f9ee Total ways from this state
            dp[(i, total)] = add + subtract

            return dp[(i, total)]

        # \U0001f680 Start recursion from index 0 with total sum = 0
        return dfs(0, 0)
