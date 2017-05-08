"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly
once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
:type s: str
:type words: List[str]
:rtype: List[int]
"""
import timeit

start = timeit.default_timer()
class Solution(object):

    def findSubstring(self, s, words):
        word_length = len(words[0])

        concat_words = ''.join(sorted(''.join(words)))
        concat_length = len(concat_words)

        possible_positions = []

        for i in range(0,len(s)-concat_length+1):
            sub = s[i:i+concat_length]
            substring = ''.join(sorted(sub))

            if substring == concat_words:
                possible_positions.append(i)
        print possible_positions
        for i in possible_positions:
            result_words = s[i:i+concat_length]
            word_list = []
            test_words = words
            for k in range(0,len(result_words),word_length):
                potential_word = result_words[k:k+word_length]
                word_list.append(potential_word)
            if set(word_list)!=set(words):
                possible_positions.remove(i)
        return possible_positions


Sol = Solution()
with open('30_test2.txt','r') as f:
    k = f.readlines()
    words = k[1].strip()
    final_list = [x.strip('"') for x in words.split(',')]
    print Sol.findSubstring(k[0],final_list)
stop = timeit.default_timer()

print stop - start
#print Sol.findSubstring("barfoothefoobarman",["foo","bar"])
