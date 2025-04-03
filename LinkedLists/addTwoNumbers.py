# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans=ListNode(-1)
        temp=ans
        carry=0
        while l1 or l2:
            new_val=l1.val + carry if not l2 else  l2.val+carry if not l1 else l1.val+l2.val +carry
            new_node=ListNode(new_val%10)
            temp.next=new_node
            temp=temp.next
            carry=new_val//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            temp.next=ListNode(carry)
        return ans.next