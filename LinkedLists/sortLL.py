# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    Below solution is working but time limit is exceeding in case of longer lists
    """
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                new_head = head.next
                head.next.next = head
                head.next = None
                return new_head
            return head

        temp = self.sortList(head.next)
        if temp.val > head.val:
            head.next = temp
            return head
        new_head = temp
        while head and temp.next and head.val > temp.next.val:
            temp = temp.next
        head.next = temp.next
        temp.next = head

        return new_head

    """
    Below solution is using merge sort technique..
    """
    def sortList_merge_sort(self,head):
        """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """

        def divide(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            right = slow.next
            left = head
            slow.next = None

            return left, right

        def merge(head1, head2):
            dummy_node = Node(-1)
            temp = dummy_node
            while head1 and head2:
                if head1.val <= head2.val:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next
            if head1:
                temp.next = head1
            if head2:
                temp.next = head2
            print("----")
            return dummy_node.next

        if not head or not head.next:
            return head

        head1, head2 = divide(head)
        head1 = self.sortList_merge_sort(head1)
        head2 = self.sortList_merge_sort(head2)

        return merge(head1, head2)







