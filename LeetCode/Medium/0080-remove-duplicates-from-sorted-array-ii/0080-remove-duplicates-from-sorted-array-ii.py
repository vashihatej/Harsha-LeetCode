class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for i in range(0,len(nums)):
            if l < 2 or nums[i] !=nums[l-2]:
                nums[l]=nums[i]
                l+=1
            else:
                count=0
                continue
        return l