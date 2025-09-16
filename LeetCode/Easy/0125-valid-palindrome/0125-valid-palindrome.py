class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res=""
        # for c in s:
        #     if c.isalnum() == True:
        #         char=c.lower()
        #         res += char
        # res = list(res)
        # return res == res[::-1]
        # start=0
        # end=len(s)-1
        # s=s.lower()
        # while start<end:
        #     if not s[start].isalnum():
        #         start+=1
        #         continue
        #     elif not s[end].isalnum():
        #         end -= 1
        #         continue
        #     elif s[start] != s[end]:
        #         return False
        #     start +=1
        #     end-=1
        # return True
        start=0
        e=len(s)-1
        s=s.lower()
        while start<e:
            if not s[start].isalnum():
                start+=1
                continue
            elif not s[e].isalnum():
                e-=1
                continue
            elif s[start]!=s[e]:
                return False
            start+=1
            e-=1
        return True
            
            

        