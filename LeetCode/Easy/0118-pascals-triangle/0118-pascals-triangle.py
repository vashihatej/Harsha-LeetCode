class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #In pascal triangle it will be always starts with 1 in first row
        #then we will create as many rows they have requested and for that we will take temp array to append two 0's at the either ends to make it simple(temp = [0] + res [-1] + [0]) and then traverse throw the before array res[-1] and add two adjacent numbers and then we add that row to the res
        res =[[1]]
        for i in range (numRows - 1):
            temp = [0] + res [-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append (temp[j] + temp[j + 1])
            res.append (row)
        return res