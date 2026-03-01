class Solution:
    def generate(self, numRows: int):
        result = []

        # Loop through each row
        for i in range(numRows):
            
            # Step 1: Create row filled with 1s
            # Every row has i+1 elements
            row = [1] * (i + 1)

            # Step 2: Fill middle values (skip first and last)
            for j in range(1, i):
                # Each element = sum of two elements above it
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            # Add row to result
            result.append(row)

        return result