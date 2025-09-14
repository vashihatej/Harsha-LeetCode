class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev=0, 1, 1, ""
        if len(arr)==1:
            return 1

        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r+=1
                prev=">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r+=1
                prev="<"
            else:
                if arr[r] == arr[r-1]:  #Handling the case when it is "="
                    r+=1
                    l=r-1
                    prev= ""
                else:
                    l=r-1
                    prev= ""


        return res