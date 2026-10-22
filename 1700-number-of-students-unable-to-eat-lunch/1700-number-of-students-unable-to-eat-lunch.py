class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
            sandwiches=deque(sandwiches)
            q=deque(students)
            i=0
            while q and i<len(q):
                if q[0]==sandwiches[0]:
                    q.popleft()
                    sandwiches.popleft()
                    i=0
                else:
                    x=q.popleft()
                    q.append(x)
                    i+=1
            return len(q)
            

                    
