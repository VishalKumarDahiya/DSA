
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self, head):
        # Returns new head of linked List.
        def add_one(head):
            """
            This is helper function
            :param head:
            :return:
            """
            if not head:
                return head
            if not head.next:
                head.data += 1
                return head

            next_head = add_one(head.next)
            if next_head and next_head.data == 10:
                next_head.data = 0
                head.data += 1
            return head

        head = add_one(head)
        if head.data == 10:
            new_head = Node(1)
            head.data = 0
            new_head.next = head
            head = new_head
        return head
