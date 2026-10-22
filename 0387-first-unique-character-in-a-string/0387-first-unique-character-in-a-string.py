class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        q=deque()
        for i,ch in enumerate(s):
            if freq[ch]==1:
                return i
        else:
            return -1