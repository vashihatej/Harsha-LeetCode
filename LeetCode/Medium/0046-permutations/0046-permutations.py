class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        freq={}
        #initialize all the distinct numbers in hashmap with frequencies 0
        for i in nums:
            freq[i] = 0
        def dfs(sub, freq):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            #at every stage check whcih and all numbers can be added and add those to subset
            for i in nums:
                if freq[i] == 0:
                    #add the number is not used earlier and call dfs for finding next permutation
                    sub.append(i)
                    freq[i]=1
                    dfs(sub, freq)
                    sub.pop()
                    freq[i]=0
        dfs([], freq)
        return res
