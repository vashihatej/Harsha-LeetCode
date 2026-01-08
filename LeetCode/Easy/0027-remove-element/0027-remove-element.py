class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # l =0
        # while val in nums:
        #     nums.remove(val)
        # l = len(nums)
        # return l
        l=0
        for n in nums:
            if n != val:
                nums[l]=n
                l+=1
        return l