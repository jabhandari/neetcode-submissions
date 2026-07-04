# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid of the list
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second half of list
        #second will act as curr
        second=slow.next
        prev=None
        slow.next=None #break the link split the list in 2 parts
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        #merge links alternatively
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2