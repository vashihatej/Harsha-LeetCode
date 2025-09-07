class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # n = len(students)
        # count = Counter(students)
        # res = n

        # for s in sandwiches:
        #     if count[s] > 0:
        #         count[s] -= 1
        #         res-=1
        #     else:
        #         break
        # return res

        n = len(students)
        q = deque(students)

        res = n
        for s in sandwiches:
            cnt=0
            while cnt<n and s != q[0]:
                temp = q.popleft()
                q.append(temp)
                cnt+=1
            if s == q[0]:
                q.popleft()
                res-=1
            else:
                break
        return res


