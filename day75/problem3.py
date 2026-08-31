# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points



def nodesBetweenCriticalPoints(head):
    currpos=0
    curr=head
    firstpos=None
    prevpos=None
    prevvalue=curr.val
    curr=curr.next
    localmaxima=-float("inf")
    localminima=float("inf")
    while curr!=None:
        if curr.next != None:
            if prevvalue<curr.val>curr.next.val or prevvalue>curr.val<curr.next.val:
                if firstpos==None:
                    firstpos=currpos
                    prevpos=currpos
                else:
                    localmaxima=max(localmaxima,abs(firstpos-currpos))
                    localminima=min(localminima,abs(currpos-prevpos))
                    prevpos=currpos
        currpos+=1
        prevvalue=curr.val
        curr=curr.next
    if localminima==float("inf"):
        return [-1,-1]
    return [localminima,localmaxima]