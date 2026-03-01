class Solution:
    def decodeString(self, s: str) -> str:
        """
        We use a stack to decode nested patterns like:
            k[encoded_string]

        Idea:
        - Push characters into stack.
        - When we see ']', we:
            1) Pop characters until '[' to form substring.
            2) Pop digits before '[' to get repeat count.
            3) Repeat substring k times.
            4) Push result back into stack.
        """

        stack = []

        for char in s:

            # --------------------------------------------------
            # CASE 1: If character is NOT ']'
            # Just push it to stack.
            # --------------------------------------------------
            if char != ']':
                stack.append(char)

            # --------------------------------------------------
            # CASE 2: If character is ']'
            # Time to decode something.
            # --------------------------------------------------
            else:
                substr = ""

                # 1️⃣ Build the substring inside brackets
                # Pop until '['
                # We build substring in reverse order,
                # so we prepend popped characters.
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr

                stack.pop()  # Remove the '['

                # 2️⃣ Now extract the number (k)
                # It may have multiple digits (e.g., 12[abc])
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # 3️⃣ Repeat substring k times
                repeated = int(k) * substr

                # 4️⃣ Push the expanded string back to stack
                stack.append(repeated)

        # Final result is everything joined together
        return "".join(stack)