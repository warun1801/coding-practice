'''
2131. Longest Palindrome by Concatenating Two Letter Words
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''


from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        for word in words:
            d[word] += 1 


        ans = 0

        s = set(d.keys())
        oddSelect = False
        for word in s:
            if word[0] == word[1]:
                if d[word] & 1:
                    oddSelect = max(oddSelect, d[word])
                    ans += (d[word] // 2) * 4
                else:
                    ans += 2 * d[word]
                d.pop(word)

        if oddSelect:
            ans += 2
        s = set(d.keys())

        for top in s:
            ans += min(d[top], d[top[::-1]]) * 4
            if top in d:
                d.pop(top)
            if top[::-1] in d:
                d.pop(top[::-1])

        return ans
