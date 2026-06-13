from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                if abs(stk[-1]) < abs(a):
                    stk.pop()
                elif abs(stk[-1]) == abs(a):
                    stk.pop()
                    break
                else:
                    break
            else:
                stk.append(a)
        return stk