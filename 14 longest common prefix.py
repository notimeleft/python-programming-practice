'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #edge cases 
        if len(strs)<2:
            if not strs:
                return ""
            return strs[0]
        #sort the strings and find the longest possible shared prefix, i.e the first element
        strs.sort()
        prefix = strs[0]
        
        #longest common prefix is empty!
        if not prefix:
            return ""
        
        #check if prefix works for all words. If not, shorten prefix and try again. 
        for i in xrange(len(prefix)-1,-1,-1):
            k = prefix[:i+1]
            if self.check_prefix(k,strs):
                return k
        
        #no prefixes in common!
        return ""
    def check_prefix(self,prefix,words):
        for x in words:
            if not x.startswith(prefix):
                return False
        return True        