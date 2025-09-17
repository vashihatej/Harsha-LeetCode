from typing import List, Dict, Set

class TrieNode:
    def __init__(self):
        # Each node has children (char -> TrieNode)
        self.children = {}
        # Marks if a full word ends at this node
        self.isWord = False

    def addWord(self, word):
        # Insert a word into the Trie character by character
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # Mark the last character node as the end of a word
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie from the given list of words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # res = words found, visit = cells currently in DFS path

        def dfs(r, c, node, word):
            """
            DFS from position (r, c) following Trie 'node' with current string 'word'
            """
            # Boundary checks + visited check + check if letter exists in Trie
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children):
                return

            # Mark this cell as visited
            visit.add((r, c))
            # Move to the child node for this character
            node = node.children[board[r][c]]
            # Add character to current path
            word += board[r][c]

            # If this node represents a word, add it to results
            if node.isWord:
                res.add(word)

            # Explore all 4 neighbors
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack: unmark this cell before returning
            visit.remove((r, c))

        # Start DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # Convert set to list before returning
        return list(res)
