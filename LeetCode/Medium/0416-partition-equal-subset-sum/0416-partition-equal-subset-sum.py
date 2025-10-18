class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Step 1️⃣ — Compute total sum
        total = sum(nums)
        
        # If total is odd, we cannot split it evenly
        if total % 2:
            return False
        
        target = total // 2        # Each subset should sum to this
        n = len(nums)
        
        # Step 2️⃣ — Initialize DP table with -1 (uncomputed)
        # dp[i][t] means: can we reach sum 't' using elements from index i onward?
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        # Step 3️⃣ — Define recursive DFS function
        def dfs(i, target):
            # Base case: if we've processed all items
            if i >= n:
                return target == 0  # return True if we've exactly hit the target
            
            # If target becomes negative → invalid path
            if target < 0:
                return False
            
            # If already computed → reuse result
            if dp[i][target] != -1:
                return dp[i][target]
            
            # Choice 1: skip current number
            skip = dfs(i + 1, target)
            
            # Choice 2: include current number (subtract its value)
            include = dfs(i + 1, target - nums[i])
            
            # Store whether any of the choices worked
            dp[i][target] = skip or include
            return dp[i][target]
        
        # Step 4️⃣ — Start recursion from index 0 with full target
        return dfs(0, target)
