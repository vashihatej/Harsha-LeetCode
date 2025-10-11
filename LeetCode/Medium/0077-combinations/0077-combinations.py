class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(i, sub, res, n, k):
            if len(sub) == k:
                res.append(sub.copy())
                return
            if i >n :
                return
            for j in range(i, n+1):
                sub.append(j)
                back(j+1, sub, res, n, k)
                sub.pop()
        back(1, [], res, n, k)
        return res
