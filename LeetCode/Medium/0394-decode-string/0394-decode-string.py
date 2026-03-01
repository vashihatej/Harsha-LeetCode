class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c != ']':
                stack.append(c)
            if c == ']':
                curstr=""
                while stack and stack[-1]!='[':
                    curstr=stack.pop()+curstr
                stack.pop()
                curnum=""
                while stack and stack[-1].isdigit():
                    curnum=stack.pop()+curnum
                stack.append(int(curnum)*curstr)
        return ''.join(stack)
            