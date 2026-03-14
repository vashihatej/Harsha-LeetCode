from typing import List

# ----------------------------
# Trie Node (single character)
# ----------------------------
class TrieNode:
    def __init__(self):
        # children maps character -> TrieNode
        self.children = {}
        # isWord is True if a complete word ends at this node
        self.isWord = False


# ----------------------------
# Trie Data Structure
# ----------------------------
class Trie:
    def __init__(self):
        # Root node represents empty prefix
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Insert a word into the Trie character by character.
        """
        cur = self.root
        for c in word:
            # Create child node if it does not exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node
            cur = cur.children[c]

        # Mark the last node as a complete word
        cur.isWord = True


# ----------------------------
# Main Solution
# ----------------------------
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie from given words
        trie = Trie()
        for word in words:
            trie.addWord(word)

        root = trie.root
        ROWS, COLS = len(board), len(board[0])

        # Set to store found words (avoids duplicates)
        result = set()
        # Set to track visited board cells during DFS
        visited = set()

        def dfs(r: int, c: int, node: TrieNode, path: str):
            """
            DFS from board[r][c], following Trie node,
            building the current word 'path'.
            """

            # Boundary checks
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            # Mark current cell as visited
            visited.add((r, c))

            # Move to the Trie child node
            node = node.children[board[r][c]]
            # Append character to path
            path += board[r][c]

            # If this Trie node completes a word, add to result
            if node.isWord:
                result.add(path)

            # Explore all 4 directions
            dfs(r + 1, c, node, path)  # down
            dfs(r - 1, c, node, path)  # up
            dfs(r, c + 1, node, path)  # right
            dfs(r, c - 1, node, path)  # left

            # Backtrack: unmark visited cell
            visited.remove((r, c))

        # 2. Start DFS from every board cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # Convert set to list and return
        return list(result)

