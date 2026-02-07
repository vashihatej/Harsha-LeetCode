class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # L=0
        # window=set()
        # for R in range(len(nums)):
        #     if nums[R] in window:    
        #         return True
        #     window.add(nums[R])
        #     if R-L+1 > k:
        #         window.remove(nums[L])
        #         L+=1

        # return False







        L=0
        window_set = set()
        for R in range(len(nums)):
            if nums[R] in window_set:
                return True
            window_set.add(nums[R])
            if R-L+1 > k:
                window_set.remove(nums[L])
                L+=1
        return False