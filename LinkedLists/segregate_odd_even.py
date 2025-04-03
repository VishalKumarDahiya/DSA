# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        head1 = odd = head
        head2 = even = head.next
        while odd.next and odd.next.next and even.next and even.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        if odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        even.next = None
        odd.next = head2
        return head