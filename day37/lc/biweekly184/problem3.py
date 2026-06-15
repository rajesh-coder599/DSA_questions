# Q3. Maximum Total Value of Covered Indices©leetcode
def maxTotal(nums,s):
    mxsum=0
    n=len(s)
    st=None
    en=None
    currsum=0
    currmn=float("inf")
    for i in range(n):
        if s[i]=="1":
            if st==None:
                st=i
                en=i
            else:
                en=i
            currsum+=nums[i]
            currmn=min(currmn,nums[i])
        else:
            if st!=None:
                if st-1<0:
                    mxsum+=currsum
                    st=None
                    en=None
                    currsum=0
                    currmn=float("inf")
                else:
                    if nums[st-1]>=currmn:
                        mxsum+=(currsum+nums[st-1]-currmn)
                    else:
                        mxsum+=currsum
                    st=None
                    en=None
                    currsum=0
    if st!=None:
                if st-1<0:
                    mxsum+=currsum
                    st=None
                    en=None
                    currsum=0
                else:
                    if nums[st-1]>=currmn:
                        mxsum+=(currsum+nums[st-1]-currmn)
                    else:
                        mxsum+=currsum
                    st=None
                    en=None
                    currsum=0
                    currmn=float("inf")      
    return mxsum