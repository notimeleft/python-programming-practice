'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        #build a dict of (pattern, word) kv entries. While building the dict, return false if errors in the pattern occur. 


        words = str.split()
        if len(pattern)==len(words):
            pattern_dict = {}
            for i in xrange(0,len(pattern)):
                if pattern[i] in pattern_dict:
                    if pattern_dict[pattern[i]]!=words[i]:
                        return False
                        
                else:
                    pattern_dict[pattern[i]]=words[i]
            
            if len(pattern_dict.keys())!=len(set(pattern_dict.values())):
                return False
            return True        
        else:
            return False