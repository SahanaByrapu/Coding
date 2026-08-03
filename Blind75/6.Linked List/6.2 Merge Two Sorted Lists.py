# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1=list1
        l2=list2
        head=ListNode(-1)
        prevnode=head

        while(l1!= None and l2!=None):
           if l1.val <= l2.val:
            prevnode.next=l1
            l1=l1.next
           else:
            prevnode.next=l2
            l2=l2.next

           prevnode= prevnode.next

        prevnode.next= l1 if ( l1!= None) else l2

        return head.next

            
