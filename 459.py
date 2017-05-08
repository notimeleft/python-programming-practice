import re
from math import sqrt
from collections import Counter
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #unique elements
        k = len(set(s))
        #if s has 1 letter, or s is a string of unique characters, it's always false
        if(len(s)<2 or len(s)==k): return False
        #if s has 1 unique element, it's always true
        if(k==1): return True
       
        #check the first x letters of the string for a possible word match. Each x is a factor of the length of s. 
        check = self.factors(len(s))
        
        for x in check:
            match = re.sub(s[:x],"",s)
            
            if(len(match)==0): return True 
        return False    
    
    #find all factors of a number, upper limit is sqrt to limit computation     
    def factors(self,n):
        fac = []
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                fac.append(i)
                fac.append(n/i)     
        return fac        
            