class Solution:
    def calPoints(self, op: List[str]) -> int:
        r=[]
        for i in op:
            if i=="C":
                r.pop()
            elif i=="D":
                r.append(r[-1] *2)
            elif i=="+":
                r.append(r[-1]+r[-2])
            else:
                r.append(int(i))
        return sum(r)
