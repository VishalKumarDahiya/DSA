"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping={}
        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]]+=1
            else:
                mapping[s[i]]=1
            if t[i] in mapping:
                mapping[t[i]]-=1
            else:
                mapping[t[i]]=-1

        print(mapping)
        for m in mapping:
            if mapping[m]:
                return False
        return True


s="anagram"
t="nagaram"
sol= Solution()
print(sol.isAnagram(s,t))

"""
This can also be done by sorting both the strings and directly comparing the equality
"""