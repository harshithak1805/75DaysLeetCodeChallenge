class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        if digits[i]!=0:
                            x=digits[i]*100 + digits[j]*10 + digits[k]
                            if (x) %2==0:
                                res.add(x)
        return sorted(res)

