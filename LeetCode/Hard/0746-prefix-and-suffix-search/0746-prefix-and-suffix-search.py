class WordFilter:

    def __init__(self, words: List[str]):
        """
        Precompute all (prefix, suffix) combinations for each word
        and store them in a hashmap.

        Key format: "prefix + '$' + suffix"
        Value: the index of the word in the original list.

        Since we overwrite with each word's index as we go, the map
        always stores the **largest index** (requirement in problem).
        """
        self.mp = {}

        for i, w in enumerate(words):
            # Try every possible non-empty prefix of word w
            for j in range(len(w)):
                pref = w[:j + 1]

                # Try every possible suffix of word w
                for k in range(len(w)):
                    # Construct a unique key combining prefix + '$' + suffix
                    cur = pref + "$" + w[k:]

                    # Store or overwrite index → ensures largest index kept
                    self.mp[cur] = i

    def f(self, pref: str, suff: str) -> int:
        """
        Query in O(1) average time:
        - Build the key from pref + '$' + suff
        - If it exists in our map, return the stored index
        - Otherwise return -1 (no such word exists)
        """
        s = pref + "$" + suff
        if s not in self.mp:
            return -1
        return self.mp[s]
