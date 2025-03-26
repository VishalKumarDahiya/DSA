"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapping={}
        for a in s:
            if a in mapping:
                mapping[a]+=1
            else:
                mapping[a]=1

        mapping2={}
        for m in mapping:
            if mapping[m] in mapping2:
                mapping2[mapping[m]].append(m)
            else:
                mapping2[mapping[m]]=[m]

        res=""
        for i in range(len(s),0,-1):
            if i in mapping2:
                res+="".join([a*i for a in mapping2[i]])
        return res

sol=Solution()
s = "Aabb"
sol.frequencySort(s)


