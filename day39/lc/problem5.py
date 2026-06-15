# 2095. Delete the Middle Node of a Linked List


def deleteMiddle(head):
    if not head.next:
        return
    n=0
    curr=head
    while curr:
        n+=1
        curr=curr.next
    n//=2
    curr=head
    prev=None
    for _ in range(n):
        prev=curr
        curr=curr.next
    curr=curr.next
    prev.next=curr
    return head