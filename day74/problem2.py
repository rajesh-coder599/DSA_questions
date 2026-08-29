# 729. My Calendar I


class MyCalendar:

    def __init__(self):
        self.calendar=[]      

    def book(self, startTime, endTime):
        for s,e in self.calendar:
            if max(s,startTime)<min(e,endTime):
                return False
        self.calendar.append([startTime,endTime])
        return True