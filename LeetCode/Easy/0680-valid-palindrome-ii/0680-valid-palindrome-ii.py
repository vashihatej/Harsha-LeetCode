class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Two pointer approach.

        If mismatch occurs,
        try skipping either left OR right character.
        """

        def isPalindrome(l, r):
            # Check if substring s[l:r] is palindrome
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # We have one chance to delete a character
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l += 1
            r -= 1

        return True