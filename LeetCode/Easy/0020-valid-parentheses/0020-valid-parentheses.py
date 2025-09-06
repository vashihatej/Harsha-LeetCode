class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        brac_map={')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in brac_map:
                if  not stack or brac_map[i] != stack[-1]:
                    return False
                stack.pop()
                    
            else:
                stack.append(i)
        return not stack