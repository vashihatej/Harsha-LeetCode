class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(i, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            if i >n :
                return
            for j in range(i, n+1):
                sub.append(j)
                back(j+1, sub)
                sub.pop()
        back(1, [])
        return res
