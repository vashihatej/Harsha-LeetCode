class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # res = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
        #     #decision to include nums[i] at every step
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     #decision not to include nums[i] at every step
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)

        # return res

        res=[]
        def dfs(i, arr):
            if i>=len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.remove(nums[i])
            dfs(i+1, arr)
        dfs(0, [])
        return res

