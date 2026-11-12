# 2409. Count Days Spent Together



def countDaysTogether(arriveAlice,leaveAlice,arriveBob,leaveBob):
    month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    prefix=[0]
    for i in range(12):
        prefix.append(prefix[-1]+month[i])
    
    days=0
    aa=prefix[int(arriveAlice[:2])-1]+int(arriveAlice[3:])
    la=prefix[int(leaveAlice[:2])-1]+int(leaveAlice[3:])
    ab=prefix[int(arriveBob[:2])-1]+int(arriveBob[3:])
    lb=prefix[int(leaveBob[:2])-1]+int(leaveBob[3:])
    if ab>la or aa>lb :
        return 0
    start=max(aa,ab)
    end=min(la,lb)
    return end-start+1