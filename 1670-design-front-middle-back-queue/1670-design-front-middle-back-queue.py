class FrontMiddleBackQueue:

    def __init__(self):
        self.res=[]

    def pushFront(self, val: int) -> None:
        self.res.insert(0,val)

    def pushMiddle(self, val: int) -> None:
        self.res.insert(len(self.res)//2,val)

    def pushBack(self, val: int) -> None:
        self.res.insert(len(self.res),val)

    def popFront(self) -> int:
        if self.res:
            return self.res.pop(0)
        else:
            return -1
    def popMiddle(self) -> int:
        if self.res:
            return self.res.pop((len(self.res)-1 )//2)
        else:
            return -1

    def popBack(self) -> int:
        if self.res:
            return self.res.pop(-1)
        else:
            return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()