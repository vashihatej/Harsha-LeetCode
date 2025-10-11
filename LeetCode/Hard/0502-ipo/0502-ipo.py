class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap=[]
        minheap=[(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minheap)

        for i in range(k):
            while minheap and minheap[0][0] <= w:
                c, p=heapq.heappop(minheap)
                heapq.heappush(maxheap, -1*p)
            if not maxheap:
                break
            w+= -1*heapq.heappop(maxheap)
            
        return w
