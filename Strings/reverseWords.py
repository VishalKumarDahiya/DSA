"""
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        i=0
        while(i<len(s)):
            while i<len(s) and s[i]== " "  :
                i+=1
            j=i+1
            while j<len(s) and s[j]!= " ":
                j+=1

            if s[i:j]:
                arr.append(s[i:j])
            i=j+1

        return " ".join(arr[::-1])


s = "  hello world  "
sol=Solution()
print(len(s))
print(sol.reverseWords(s))