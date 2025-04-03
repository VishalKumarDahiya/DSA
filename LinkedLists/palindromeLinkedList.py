# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    below is the initial approach
    """
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr = []
        slow = fast = head
        arr.append(slow.val)
        while fast and fast.next:
            slow = slow.next
            arr.append(slow.val)
            fast = fast.next.next
        i = -2
        if not fast:
            i = -3
            if arr[-1] != arr[-2]:
                return False
        slow = slow.next
        while slow:
            if slow.val != arr[i]:
                return False
            i -= 1
            slow = slow.next

        return True
    def isPalindrome2(self):
        """
        Second approach can be -> reach to middle position and then reverse the second half and compare first half
        and second half, so here we will be having space complexity of O(1), constant space.
        :return:
        """
