'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
'''

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = re.sub(r'[^a-zA-Z0-9]','', s).lower()
        
        start = 0
        end = len(res)-1
        for i in xrange(0,len(res)/2):
            if res[start]!=res[end]:
                return False
            start+=1
            end-=1
        
        return True

