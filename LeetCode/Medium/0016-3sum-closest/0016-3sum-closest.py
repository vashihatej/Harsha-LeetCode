class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        cur=0
        nums.sort()
        for i in range(0, len(nums)-2):
            l=i+1
            r= len(nums)-1
            while (l<r):
                cur= nums[i]+nums[l]+nums[r]
                if abs(cur-target)< abs(target-res):
                    res=cur
                if cur>target:
                    r-=1
                elif cur==target:
                    return cur
                else:
                    l+=1
            if abs(cur-target)< abs(target-res):
                res=cur
        return res

        
        