"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3
"""


class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum=0
        current_max=0
        for a in s:
            if a == "(":
                current_max+=1
            if a==")":
                current_max-=1
            maximum=max(maximum,current_max)
        return maximum

sol=Solution()
s = "()(())((()()))"
print(sol.maxDepth(s))