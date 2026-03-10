class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        visited=set()
        visited.add(beginWord)
        queue= deque()
        queue.append(beginWord)

        level=1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word=word[:i]+c+word[i+1:]
                        if new_word==endWord:
                            return level+1
                        if new_word in wordset and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            level+=1
        return 0