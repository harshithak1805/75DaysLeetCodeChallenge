class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        sums=0
        idx=1
        tot=len(word)
        while tot>0:
            if tot>=8:
                sums+=idx*8
                tot-=8
            else:
                sums+=idx*(tot)
                tot=0
            idx+=1
        return sums


            
