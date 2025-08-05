class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in matching:
                if stack and stack[-1] == matching[c]:
                    print(c)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
       
        