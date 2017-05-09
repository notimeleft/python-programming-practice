'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        input = "1"
        for i in xrange(0,n-1):
            input = self.transform(input)
        return input    
    
        
    def transform(self,input):   
        last = input[0]
        last_count=1
        res = ""
        for i in xrange(1,len(input)):
            letter = input[i]
            if last==letter:
                last_count+=1
            else:
                res+=str(last_count)+last
                last_count=1
            last = letter
        res+=str(last_count)+str(last)        
        return res