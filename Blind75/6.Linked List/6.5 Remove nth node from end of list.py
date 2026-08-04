""" https://leetcode.com/problems/remove-nth-node-from-end-of-list/ """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if (head==None): return head

        dummyNode=ListNode(-1)
        dummyNode.next=head

        first=head

        for i in range(1,n+1):
            if(first!=None):
              first=first.next

        second=dummyNode

        while(first):
            first=first.next
            second=second.next

        second.next=second.next.next

        return dummyNode.next
