# 3414. Maximum Score of Non-overlapping Intervals


## WA by this method
def maximumWeight(intervals):
    n=len(intervals)
    a={}
    x=0
    curr_score=0
    for i in range(n):
        l,r,w=intervals[i]
        if x==0:
            curr_score+=w
            x+=1
            a[i]=[l,r,w]
        else:
            temp_score=0
            temp_idx=[]
            mnscoreidx=None
            m=0
            for k,v in a.items():
                nl,nr,nw=v
                if mnscoreidx==None:
                    mnscoreidx=[k,nw]
                elif mnscoreidx[1]<nw:
                    mnscoreidx=[k,nw]
                if nl>r or nr<l:
                    continue
                temp_idx.append(k)
                temp_score+=nw
                m+=1
            if temp_score==0:
                if x<4:
                    a[i]=[l,r,w]
                    x+=1
                    curr_score+=w
                elif mnscoreidx[1]<w:
                    del a[mnscoreidx[0]]
                    curr_score-=mnscoreidx[1]
                    a[i]=[l,r,w]
                    curr_score+=w
            else:
                if temp_score<w or (temp_score==w and m!=1):
                    for j in temp_idx:
                        del a[j]
                        x-=1
                        curr_score-=intervals[j][2]
                    curr_score+=w
                    x+=1
                    a[i]=[l,r,w]
    ans=[]
    for k in a.keys():
        ans.append(k)
    ans.sort()
    return ans

