class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq=deque()
        for i in range(len(deck)-1,-1,-1):
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(deck[i])
        return list(dq)
