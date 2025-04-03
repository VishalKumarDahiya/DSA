from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        """
        this solution is not optimal, but work for shorter DLLs

        """
        # code here
        i=head
        j=head.next
        res=[]
        if not j:
            return res
        while i and i.data<=target:
            j=i.next
            while j and j.data+i.data<=target:
                if i.data+j.data==target:
                    res.append([i.data,j.data])
                j=j.next
            i=i.next
        return res

    def findPairsWithGivenSum_Optimized(self, target: int, head: Optional['Node']) -> List[List[int]]:
        """
        This solutin is optimised and same as optimized solution of array we have done
        """
        # code here
        left = head
        right = head
        ans = []
        while right.next:
            right = right.next
        while right and left and left != right and right.next != left:
            total = left.data + right.data
            if total < target:
                left = left.next
            elif total > target:
                right = right.prev
            else:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev
        return ans
