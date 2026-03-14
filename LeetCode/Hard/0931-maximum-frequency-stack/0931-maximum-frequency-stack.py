        
from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        """
        Data structures used:

        freq[val] → frequency of each value

        group[f] → stack of values that appear exactly f times

        maxFreq → current highest frequency in the stack

        Example:

            freq = {5:3, 7:2, 4:1}

            group = {
                1: [5,7,4],
                2: [5,7],
                3: [5]
            }
        """

        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0


    def push(self, val):

        # Increase frequency of val
        self.freq[val] += 1
        f = self.freq[val]

        # Update maximum frequency seen so far
        if f > self.maxFreq:
            self.maxFreq = f

        # Add value to the stack corresponding to this frequency
        self.group[f].append(val)


    def pop(self):

        """
        Always pop from the stack with the highest frequency.
        """

        # Get most recent element with max frequency
        val = self.group[self.maxFreq].pop()

        # Reduce its frequency
        self.freq[val] -= 1

        # If no elements left at this frequency level
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()