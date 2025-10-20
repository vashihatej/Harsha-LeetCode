class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(s1, s2):
            """
            Returns the minimum edit distance needed to convert
            word1[s1:] → word2[s2:].
            """
            # \U0001f3af Base case: if we've reached the end of word1
            # We must insert all remaining characters from word2
            if s1 == len(word1):
                return len(word2) - s2

            # \U0001f3af Base case: if we've reached the end of word2
            # We must delete all remaining characters from word1
            if s2 == len(word2):
                return len(word1) - s1

            # \U0001f9e0 Return memoized result if seen before
            if (s1, s2) in dp:
                return dp[(s1, s2)]

            # \U0001f7e2 If characters match → no operation needed
            if word1[s1] == word2[s2]:
                dp[(s1, s2)] = dfs(s1 + 1, s2 + 1)

            else:
                # \U0001f534 Characters differ → try all 3 operations

                # 1️⃣ Insert word2[s2] → stay at s1, move s2
                insert_op = 1 + dfs(s1, s2 + 1)

                # 2️⃣ Delete word1[s1] → move s1, stay at s2
                delete_op = 1 + dfs(s1 + 1, s2)

                # 3️⃣ Replace word1[s1] with word2[s2] → move both
                replace_op = 1 + dfs(s1 + 1, s2 + 1)

                # Take the minimum cost operation
                dp[(s1, s2)] = min(insert_op, delete_op, replace_op)

            return dp[(s1, s2)]

        # \U0001f680 Start recursion from both indices = 0
        return dfs(0, 0)
