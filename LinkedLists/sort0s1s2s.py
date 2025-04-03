# User function Template for python3
'''
	Your task is to segregate the list of
	0s,1s and 2s.

	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''

"""
Below solution I have written but still the using  merge sort is more efficient than this one.
"""
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        temp0 = zeros = Node(-1)
        temp1 = ones = Node(-1)
        temp2 = twos = Node(-1)

        while head:
            if head.data == 0:
                temp0.next = head
                temp0 = temp0.next
            elif head.data == 1:
                temp1.next = head
                temp1 = temp1.next
            else:
                temp2.next = head
                temp2 = temp2.next
            head = head.next
        if ones.next:
            temp0.next = ones.next
        if twos.next:
            temp1.next = twos.next
        return zeros.next