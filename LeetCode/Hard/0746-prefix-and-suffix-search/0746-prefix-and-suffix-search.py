# class WordFilter:

#     def __init__(self, words: List[str]):
#         """
#         Precompute all (prefix, suffix) combinations for each word
#         and store them in a hashmap.

#         Key format: "prefix + '$' + suffix"
#         Value: the index of the word in the original list.

#         Since we overwrite with each word's index as we go, the map
#         always stores the **largest index** (requirement in problem).
#         """
#         self.mp = {}

#         for i, w in enumerate(words):
#             # Try every possible non-empty prefix of word w
#             for j in range(len(w)):
#                 pref = w[:j + 1]

#                 # Try every possible suffix of word w
#                 for k in range(len(w)):
#                     # Construct a unique key combining prefix + '$' + suffix
#                     cur = pref + "$" + w[k:]

#                     # Store or overwrite index → ensures largest index kept
#                     self.mp[cur] = i

#     def f(self, pref: str, suff: str) -> int:
#         """
#         Query in O(1) average time:
#         - Build the key from pref + '$' + suff
#         - If it exists in our map, return the stored index
#         - Otherwise return -1 (no such word exists)
#         """
#         s = pref + "$" + suff
#         if s not in self.mp:
#             return -1
#         return self.mp[s]


class TrieNode:
    def __init__(self):
        # children: char -> TrieNode
        self.children = {}
        # indices of words that pass through this node
        self.indices = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int):
        """
        Insert a word into the trie.
        At each node, store the index of the word.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.indices.append(index)

    def search(self, prefix: str):
        """
        Return list of indices of words that match the prefix.
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        return cur.indices


class WordFilter:
    def __init__(self, words: List[str]):
        # Trie for prefixes
        self.prefTrie = Trie()
        # Trie for suffixes (reversed words)
        self.suffTrie = Trie()

        for i, word in enumerate(words):
            self.prefTrie.insert(word, i)
            self.suffTrie.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        # Get all indices matching prefix
        pref_indices = self.prefTrie.search(pref)
        if not pref_indices:
            return -1

        # Get all indices matching suffix (reverse it)
        suff_indices = self.suffTrie.search(suff[::-1])
        if not suff_indices:
            return -1

        # Two pointers from the end to find largest common index
        i, j = len(pref_indices) - 1, len(suff_indices) - 1

        while i >= 0 and j >= 0:
            if pref_indices[i] == suff_indices[j]:
                return pref_indices[i]
            elif pref_indices[i] > suff_indices[j]:
                i -= 1
            else:
                j -= 1

        return -1
