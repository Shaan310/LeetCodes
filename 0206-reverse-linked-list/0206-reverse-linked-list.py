class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        cur=head
        next=None
        while cur!=None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
        