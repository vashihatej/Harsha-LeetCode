class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return ispalin(l+1,r) or ispalin(l,r-1)
            l+=1
            r-=1
            
        return True
