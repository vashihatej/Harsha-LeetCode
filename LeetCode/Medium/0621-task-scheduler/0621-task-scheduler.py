from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        countMap = Counter(tasks)
        taskHeap = [ -cnt for cnt in countMap.values()]
        
        heapq.heapify(taskHeap)

        queue = deque()

        while taskHeap or queue:
            time += 1
            if taskHeap:
                task = heapq.heappop(taskHeap)
                if task+1 :
                    queue.append([task+1, time+n])
            else:
                time = queue[0][1]

            if queue and queue[0][1] == time:
                temp = queue.popleft()
                heapq.heappush(taskHeap, temp[0])
        
        return time




        