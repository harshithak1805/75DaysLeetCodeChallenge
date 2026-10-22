class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        stk=[]
        for i in freq:
            if freq[i]==1:
                stk.append(s.index(i))
        return min(stk) if stk else -1