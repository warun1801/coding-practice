"""
30. Substring with Concatenation of All Words
Solved
Hard
Topics
premium lock icon
Companies
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

import string
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        l = len(words[0])

        ans = []
        
            

        # print(cnt)
        exta = l * len(words)
        if n > 1000:
            c = l
        else:
            c = n - exta + 1
        for x in range(c):
            i = x
            j = x
            cnt = defaultdict(int)
            for word in words:
                cnt[word] += 1
            curr_sum = 0

            while i < n and j < n:
                word = s[j : j + l]
                # print(word)
                if not word in cnt:
                    curr_sum = 0
                    cnt = defaultdict(int)
                    for word in words:
                        cnt[word] += 1
                    j += 1
                    i = j
                else:
                    if cnt[word] > 0:
                        curr_sum += 1
                        cnt[word] -= 1
                        j += l
                    else:
                        key = s[i : i + l]
                        while key != word and i < j:
                            cnt[key] += 1
                            curr_sum -= 1
                            i += l
                            key = s[i : i + l]

                        if i < j:
                            key = s[i : i + l]
                            cnt[key] += 1
                            curr_sum -= 1
                            i += l
                if curr_sum == len(words):
                    if i not in ans:
                        ans.append(i)

        return ans

        

            
