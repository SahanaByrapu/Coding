""" https://leetcode.com/problems/merge-k-sorted-lists/ """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)==0 : return None

        merged=lists[0]
        k=len(lists)
        for i in range(1,k):
          merged=self.merge2Lists(merged,lists[i])

        return merged


    def merge2Lists(self, list1,list2):    
        l1=list1
        l2=list2

        prevNode=ListNode(-1)
        head=prevNode

        while(l1 and l2):
            if (l1.val<=l2.val):
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next

            head=head.next

        head.next= l1 if(l1!=None) else l2

        return prevNode.next
