class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total //2
        n=len(nums)
        dp = [[-1]*(target+1) for i in range (len(nums)+1)]
        def dfs(i, target):
            if i >= n:
                return target == 0
            if target < 0:
                return False
            if dp[i][target] != -1:
                return dp[i][target]
            dp[i][target] = dfs(i+1, target) or dfs(i+1, target-nums[i])
            return dp[i][target]
        return dfs(0, target)