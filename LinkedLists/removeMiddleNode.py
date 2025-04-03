# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # This one is my own approach. but check next one for more optimized solution
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        before_slow = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            before_slow = slow
            slow = slow.next
        before_slow.next = slow.next
        return head

    # Below one is more optimal, one extra space is not being used here
    def delete_middle2(head):
        """
        If the list is empty or has only one node,
        return None as there is no middle node to delete
        """
        if head is None or head.next is None:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next if head.next else None

        # Move 'fast' pointer twice as fast as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head