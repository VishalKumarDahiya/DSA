# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes=set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head=head.next
        return False
    def hasCycle_tortoise_hare(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

    def detectCycleStartPoint(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def countNodesInLoop(self, head):
        # Your code here
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count

        return 0

