'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #if 0, return 0. 
        if num==0:
            return "0"
        #append to beginning of string. 
        base7 = ""
        res = abs(num)
        #mod by 7 to find the current digit, divide by 7 to move to the right by 1 digit. Add digit to string. 
        while(res>=1):
            digit = res%7
            res = res/7
            base7 = str(digit)+base7
        #look out for the negative case. 
        if(num<0):
            return "-"+base7    
        else:
            return base7
        
            