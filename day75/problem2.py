# 352. Data Stream as Disjoint Intervals



class SummaryRanges:

    def __init__(self):
        self.nums=set()
        self.mx=None
        self.mn=None
    def addNum(self, value):
        self.num.add(value)
        if self.mx==None:
            self.mx=value
        else:
            self.mx=max(self.mx,value)
        if self.mn==None:
            self.mn=value
        else:
            self.mn=min(self.mn,value)
    def getIntervals(self):
        if self.mn==None and self.mx==None:
            return []
        self.ans=[]
        self.curr_period=[]
        for i in range(self.mn,self.mx+1):
            if i in self.nums:
                if len(self.curr_period)==0:
                    self.curr_period=[i,i]
                else:
                    self.curr_period[1]=i
            else:
                if len(self.curr_period)!=0:
                    self.ans.append(self.curr_period)
                    self.curr_period=[]
        if len(self.curr_period)!=0:
            self.ans.append(self.curr_period)
        return self.ans