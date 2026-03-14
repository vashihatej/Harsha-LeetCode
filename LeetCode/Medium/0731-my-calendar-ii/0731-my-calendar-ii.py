class MyCalendarTwo:

    def __init__(self):
        self.event=[]
        self.overlaps=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.overlaps:
            if max(s,startTime)<min(e,endTime):
                return False
        for s,e in self.event:
            if max(s,startTime)<min(e,endTime):
                maxstart=max(s,startTime)
                minend=min(e,endTime)
                self.overlaps.append((maxstart,minend))
        self.event.append((startTime,endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)