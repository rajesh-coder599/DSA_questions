# 2130. Maximum Twin Sum of a Linked List

def pairSum(head):
    n=0
    nodes={}
    curr=head
    while curr:
        n+=1
        nodes[n]=curr.val
        curr=curr.next
    mxnodesum=-float("inf")
    for i in range(n//2):
        temp=nodes[i+1]+nodes[n-i]
        mxnodesum=max(mxnodesum,temp)
    return mxnodesum