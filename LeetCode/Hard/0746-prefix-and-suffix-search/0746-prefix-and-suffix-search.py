class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = {}
        for i, w in enumerate(words):
            for j in range(len(w)):
                pref = w[:j + 1]
                for k in range(len(w)):
                    cur = pref + "$" + w[k:]
                    self.mp[cur] = i

    def f(self, pref: str, suff: str) -> int:
        s = pref + "$" + suff
        if s not in self.mp:
            return -1

        return self.mp[s]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)