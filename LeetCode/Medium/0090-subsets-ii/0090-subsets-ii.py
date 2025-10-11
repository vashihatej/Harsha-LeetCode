class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # so that we can skip the 2nd repeating number and avoid duplicates

        def back(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            back(i+1, sub)
            sub.pop()

            #to avoid the duplicates we will skip the number if the same number is already being skipped 
            #in the before recursion like in [1, 2, 2] when we are skipping 2 in second recursion we will 
            #skip the 2nd 2 also
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            back(i+1, sub)
        back(0, [])
        return res
            
        