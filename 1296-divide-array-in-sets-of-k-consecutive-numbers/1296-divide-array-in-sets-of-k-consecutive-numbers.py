from collections import Counter
class Solution:
    def isPossibleDivide(self, hand: List[int], gs: int) -> bool:
        if len(hand)%gs!=0:
            return False
        else:
            c=Counter(hand)
            for i in sorted(c):
                while c[i]>0:
                    for j in range(gs):
                        if c[i+j]==0:
                            return False
                        else:
                            c[i+j]-=1
            return True
