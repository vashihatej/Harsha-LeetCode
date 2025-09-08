class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # l = 0
        # r = len(nums)-1
        # while i<=r:
        #     #sort the 0's to start
        #     if nums[i]==0:
        #         nums[l], nums[i]= nums[i], nums[l]
        #         l+=1
        #     #sort the 2's to the end of the array
        #     if nums[i]==2:
        #         nums[r], nums[i]= nums[i], nums[r]
        #         r-=1
        #         i-=1
        #     i+=1
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1