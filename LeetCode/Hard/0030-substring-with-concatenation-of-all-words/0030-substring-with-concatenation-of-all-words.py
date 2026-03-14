from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        
        # Edge case
        if not s or not words:
            return []
        
        word_len = len(words[0])                 # length of each word
        num_words = len(words)                   # total number of words
        total_len = word_len * num_words         # total substring length
        
        word_count = Counter(words)              # expected frequency of words
        
        result = []
        
        # We try starting from each possible word offset
        for offset in range(word_len):
            
            left = offset                        # left boundary of sliding window
            window_count = {}                    # counts of words inside window
            words_used = 0                       # number of valid words matched
            
            # Move window in steps of word_len
            for right in range(offset, len(s) - word_len + 1, word_len):
                
                word = s[right:right + word_len]  # extract next word
                
                # If word exists in target words
                if word in word_count:
                    
                    window_count[word] = window_count.get(word, 0) + 1
                    words_used += 1
                    
                    # If we have too many occurrences of a word
                    while window_count[word] > word_count[word]:
                        
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                        words_used -= 1
                    
                    # If window has all required words
                    if words_used == num_words:
                        result.append(left)
                
                else:
                    # Reset window if word not in words
                    window_count.clear()
                    words_used = 0
                    left = right + word_len
        
        return result
