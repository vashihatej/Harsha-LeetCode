class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # No_rows = len(matrix)
        # No_cols = len(matrix[0])

        # top, bot=0, No_rows-1
        # while top <= bot:
        #     mid_row = (top+bot)//2
        #     if target > matrix[mid_row][-1]:
        #         top = mid_row+1
        #     elif target < matrix[mid_row][0]:
        #         bot = mid_row-1
        #     else:
        #         break

        # mid_row=(top+bot)//2
        # l, r=0, No_cols-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if target > matrix[mid_row][mid]:
        #         l= mid+1
        #     elif target < matrix[mid_row][mid]:
        #         r=mid-1
        #     else:
        #         return True
        # return False
        # j=len(matrix[0])-1
        # i=0
        # while i<=len(matrix)-1 and j>=0:
        #     curval = matrix[i][j]
        #     print(matrix[i][j])
        #     if curval==target:
        #         return True
        #     elif curval<target:
        #         i+=1
        #     else:
        #         j-=1
        # return False


        i=0
        j=len(matrix[0])-1
        while i <= len(matrix)-1 and j >= 0:
            curval = matrix[i][j]
            if curval == target:
                return True
            elif curval < target:
                i +=1
            else:
                j-=1
        return False




            