class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=[]
        total=0
        for n in nums:
            total+=n
            prefixsum.append(total)
        for i in range(len(nums)):
            pre=prefixsum[i-1] if i>0 else 0
            post=prefixsum[len(nums)-1]-prefixsum[i]
            if pre == post:
                return i
        return -1
