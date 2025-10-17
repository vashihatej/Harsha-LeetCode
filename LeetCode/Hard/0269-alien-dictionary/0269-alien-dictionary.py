class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # ----------------------------------------------------
        # Step 1️⃣: Build adjacency list (graph)
        # ----------------------------------------------------
        adj = {c: set() for w in words for c in w}

        # Build edges based on first differing characters between words like in "wrt" and "wrf" we will add t -> f like add f as adjacent node to adj[t]
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # Edge case: invalid prefix (["abc", "ab"]) you cant have this as for sure abc is bigger than ab and it should come after ab
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])  # w1[j] → w2[j]
                    break  # only first difference matters yeah like "er" and "ett" only r -> t difference matters as by this difference only they are being sorted

        # ----------------------------------------------------
        # Step 2️⃣: Topological Sort Alogorithm with cycle detection
        # ----------------------------------------------------
        visit = set()      # permanently visited (no cycle)
        path = set()       # nodes in current recursion stack
        output = []        # holds topologically sorted characters

        def dfs(ch):
            # Cycle detected
            if ch in path:
                return False
            # Already processed
            if ch in visit:
                return True

            # Mark current node as being visited
            path.add(ch)

            # Visit all neighbors
            for nei in adj[ch]:
                if not dfs(nei):
                    return False  # cycle found below

            # Finished exploring → move from path to visit
            path.remove(ch)
            visit.add(ch)

            # Post-order append (topological)
            output.append(ch)
            return True

        # Run DFS for all characters
        for ch in adj:
            if not dfs(ch):
                return ""  # cycle detected → invalid dictionary

        # ----------------------------------------------------
        # Step 3️⃣: Reverse output (post-order)
        # ----------------------------------------------------
        output.reverse()
        return "".join(output)
