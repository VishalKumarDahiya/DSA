"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        current = strs[0]
        if not current:
            return current
        for s in strs[1:]:
            if not s:
                return s
            i=0
            while i <min(len(current), len(s)):
                if current[i] != s[i]:
                    break
                i+=1
            current = current[:i]
            if not current:
                return current
        return current

sol=Solution()
strs=["dog","racecar","car"]

print(sol.longestCommonPrefix(strs))


"""
this can also be solved by sorting the array and then comparing first and last elements.
"""