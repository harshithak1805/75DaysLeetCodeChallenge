import heapq
class MedianFinder:

    def __init__(self):
        self.mf=[]
        
    def addNum(self, num: int) -> None:
        self.mf.append(num)

    def findMedian(self) -> float:
        n=len(self.mf)
        self.mf.sort()
        if len(self.mf)%2==0:
            return (self.mf[n//2]+self.mf[n//2 -1]) /2
        else:
            return self.mf[n//2]
     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()