# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head
        temp = None
        while curr:
            next_node = curr.next
            curr.next = temp
            temp = curr
            curr = next_node
        return temp
    
    def reverseList_Recursive(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head
        new_head=self.reverseList_Recursive(head.next)
        temp=new_head
        while temp.next:
            temp=temp.next
        temp.next=head
        head.next=None
        return new_head





