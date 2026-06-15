# 143. Reorder List


def reorderList(head):
    if not head.next or not head.next.next:
        return head
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    if fast:
        slow=slow.next
    prev=slow
    slow=slow.next
    prev.next=None
    prv=None
    nxt=None
    curr=slow
    while curr:
        nxt=curr.next
        curr.next=prv
        prv=curr
        curr=nxt
    first=head
    second=prv
    while second:
        a=first.next
        b=second.next
        second.next=a
        first.next=second
        second=b
        first=a
    return head