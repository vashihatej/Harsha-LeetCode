# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        #Left Bisect
        #Normal Binary search itself but instead ending that when we get any match for the target instead continue until the end where l and r crosses and that when it crossing, the mid is the value we want. 
        while l<r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        return l