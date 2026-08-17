# 4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights




def minPenalty(period,lights,arrivalTime):
    x=max(lights)
    mxpenalty=0
    for i in arrivalTime:
        r=i%period
        if r>=x:
            mxpenalty=max(mxpenalty,period-r)
    return mxpenalty