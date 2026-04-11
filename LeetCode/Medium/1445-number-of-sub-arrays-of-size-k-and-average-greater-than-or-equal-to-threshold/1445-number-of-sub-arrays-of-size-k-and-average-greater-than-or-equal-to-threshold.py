class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L=0
        sum=0
        count = 0
        for R in range(len(arr)):
            sum+=arr[R]
            if R-L+1 > k:
                sum-=arr[L]
                L+=1
            if (sum /k) >= threshold and R-L+1 == k:
                count+=1
        return count


        # L=0
        # sum=0
        # count=0
        # for R in range(len(arr)):
        #     sum+=arr[R]
        #     print("sum", sum)
        #     if (sum/k)>=threshold and R-L+1 ==k:
        #         count+=1

        #     print("count",count)
        #     print(R-L+1)

        #     if R-L+1 > k:
        #         sum-=arr[L]
        #         L+=1
        # return count
