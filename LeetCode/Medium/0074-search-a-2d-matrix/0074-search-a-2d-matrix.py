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

        rows=len(matrix)
        col=len(matrix[0])
        start = 0
        end= (rows*col)-1

        while start<=end:
            mid=(start+end)//2
            midele=matrix[mid//col][mid%col]
            if midele==target:
                return True
            elif midele>target:
                end=mid-1
            else:
                start=mid+1
        return False







            