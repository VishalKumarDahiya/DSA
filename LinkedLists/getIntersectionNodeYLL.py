# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    First solution i have written is using hashmap as extra space
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        mapping = set()
        while headA and headB:
            if headA == headB:
                return headA
            elif headA in mapping:
                return headA
            elif headB in mapping:
                return headB
            else:
                mapping.add(headA)
                mapping.add(headB)
                headA = headA.next
                headB = headB.next
        while (headA):
            if headA in mapping:
                return headA
            else:
                mapping.add(headA)
                headA = headA.next
        while (headB):
            if headB in mapping:
                return headB
            else:
                mapping.add(headB)
                headB = headB.next
        return None

    """
    second solution I am finding the lenght of each LL and then making a simultanious move by 
    adjusting longer one
    """
    def getIntersectionNode2(self,headA,headB):
        l1=l2=0
        temp=headA
        while temp:
            l1+=1
            temp=temp.next

        temp = headB
        while temp:
            l2 += 1
            temp = temp.next
        d=l1-l2
        if d>0:
            while(d):
                headA=headA.next
                d-=1
        else:
            while(d):
                headB=headB.next
                d+=1
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next

        return None

    """
    one more better approach is there where we are not even calculating length first
    """
    def getIntersectionNode3(self,headA,headB):
        h1=headA
        h2=headB
        while h1 != h2:
            h1=headB if not h1 else h1.next
            h2=headA if not h2 else h2.next
        return h1



