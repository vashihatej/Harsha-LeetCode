class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        count = Counter(students)
        res = n
        print(count)

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                res-=1
            else:
                break
        return res