class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        ml=0
        for i in range(len(s)):
            if s[i]==")":
                stk.pop()
                if stk :
                        ml=max(ml,i-stk[-1])
                else:
                    stk.append(i)
            else:
                stk.append(i)
        return ml



