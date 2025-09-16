class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixsum=[]
        total=0
        for n in nums:
            total+=n
            prefixsum.append(total)
        for i in range(len(nums)):
            pre=prefixsum[i-1] if i>0 else 0 #to fix the edge case when the answer is at 0th index and 0-1 will become array[-1] which is last element instead of considering 0 to the left side of the 0th index element
            post=prefixsum[len(nums)-1]-prefixsum[i]
            if pre == post:
                return i
        return -1
