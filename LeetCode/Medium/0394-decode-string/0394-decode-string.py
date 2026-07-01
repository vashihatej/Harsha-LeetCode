class Solution:
    def decodeString(self, s: str) -> str:
        number=[]
        string=[]
        cur_num=0
        cur_str=''
        for c in s:
            if c.isdigit():
                cur_num=cur_num*10+int(c)
            elif c=='[':
                number.append(cur_num)
                string.append(cur_str)
                cur_num=0
                cur_str=''
            elif c==']':
                last_num=number.pop()
                last_str=string.pop()
                cur_str=last_str+cur_str*last_num
                

            else:
                cur_str=cur_str+c
        return cur_str

        