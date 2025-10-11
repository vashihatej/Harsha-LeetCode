class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        #map the each number with respective charaters
        digitTOchar = { "2" : "abc",
                        "3" : "def",
                        "4" : "ghi",
                        "5" : "jkl",
                        "6" : "mno",
                        "7" : "qprs",
                        "8" : "tuv",
                        "9" : "wxyz"
        }

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            #recursively check for each character in the characters mapped to digit in position i like
            #for digit "23" 2 is mapped to abc and for each char a, b, c then go recursively for "a" with 
            #cahracters mapped to digit 3 "def" like "ad", "ae", "af"
            for c in digitTOchar[digits[i]]:
                backtrack(i+1, curstr+c)
# check for if digits is empty
        if digits:
            backtrack(0, "")
        return res