class Solution:
    def longestPalindrome(self, s: str) -> str:
        #the logic here is we will imagine the character we are in as a center of a substring and will move both sides checking until what lenght it is palindrome like ex "cbabd" when we are in i =2 means at "a" we will move l and r until "b" at each side and store that 
        res = ""
        longest = 0
        for i in range(len(s)):
            #for odd number of characters in resulting substring
            l, r = i, i 
            while l>=0 and r <=len(s)-1 and s[l] == s[r]:           #the l and r should not go out of bound and it should be palindrome 
                if r-l+1 > longest:
                    res = s[l:r+1]                          #updating the res with current longest substring
                    longest = r-l+1
                l-=1
                r+=1
            
            #for even number of characters in resulting substring this is a edge case for example sring = "abb" so to find bb we need to implement this
            l, r = i, i+1
            while l>=0 and r <=len(s)-1 and s[l] == s[r]:
                if r-l+1 > longest:
                    res = s[l:r+1]
                    longest = r-l+1
                l-=1
                r+=1
        return res
        