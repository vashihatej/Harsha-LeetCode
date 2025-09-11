class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []

        # def dfs(i, subset, targetsum):
        #     if targetsum == target:
        #         res.append(subset.copy())
        #         return
        #     if targetsum > target or i >= len(candidates):
        #         return
            
        #     subset.append(candidates[i])
        #     targetsum+=candidates[i]
        #     dfs(i, subset, targetsum)
        #     subset.pop()
        #     targetsum-=candidates[i]
        #     dfs(i+1, subset, targetsum)

        # dfs(0, [], 0)
        # return res

        # res = []
        # subset = []

        # def dfs(i, current_sum):
        #     if current_sum == target:
        #         res.append(subset.copy())
        #         return
        #     if current_sum > target or i >= len(candidates):
        #         return
            
        #     # Include the current candidate
        #     subset.append(candidates[i])
        #     dfs(i, current_sum + candidates[i])
        #     # Backtrack by removing the last added candidate
        #     subset.pop()
            
        #     # Skip the current candidate
        #     dfs(i + 1, current_sum)

        # # Start the recursive function
        # dfs(0, 0)
        # return res


        res=[]
        def dfs(i, arr, sum):
            if sum == target:
                res.append(arr.copy())
                return
            if i>=len(candidates) or sum > target:
                return
            arr.append(candidates[i])
            dfs(i, arr, sum+candidates[i])         #can Include same index element multiple times here
            arr.remove(candidates[i])
            dfs(i+1, arr, sum)         #Dont Include the element in index i
        dfs(0, [], 0)
        return res






        