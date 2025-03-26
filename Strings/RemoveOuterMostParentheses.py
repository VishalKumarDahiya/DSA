"""
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""

class Solution(object):
    def removeOuterParentheses(self,s):
        res=""

        mapping={
            "(": 1,
            ")": -1
        }
        count=0
        for a in s:
            if count>1 or (count==1 and a!=")"):
                res+=a
            count += mapping[a]

        return res

sol=Solution()
s = "(()())(())(()(()))"
print(sol.removeOuterParentheses(s))





