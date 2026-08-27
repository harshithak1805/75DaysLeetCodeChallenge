class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ps=[-1]*n
        stk1=[]
        for i in range(n):
            while stk1 and heights[stk1[-1]]>=heights[i]:
                stk1.pop()
            if stk1:
                ps[i]=stk1[-1]
            stk1.append(i)
        ns=[n]*n
        stk2=[]
        for i in range(n-1,-1,-1):
            while stk2 and heights[stk2[-1]]>=heights[i]:
                stk2.pop()
            if stk2:
                ns[i]=stk2[-1]
            stk2.append(i)
        area=float("-inf")
        for i in range(n):
            area=max(area,(heights[i]*(ns[i]-ps[i]-1)))
        return area