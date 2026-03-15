class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

#---------------------------#
class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        We use a stack to simulate removing adjacent duplicates.

        Idea:
        - Traverse the string character by character.
        - Keep a stack of characters that remain in the string.

        For each character:
            If the stack is NOT empty AND
               the top of stack equals the current character

            → we found adjacent duplicates
            → remove the previous character (pop)

            Otherwise:
            → push the current character

        The stack always represents the current valid string.
        """

        stack = []

        for ch in s:

            # If stack has elements and the top matches current char
            if stack and stack[-1] == ch:
                # remove duplicate pair
                stack.pop()

            else:
                # otherwise keep the character
                stack.append(ch)

        # Join remaining characters
        return "".join(stack)