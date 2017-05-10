'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''

from math import sqrt
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return False
        divisors= [1]
        for i in xrange(2,int(sqrt(num)+1)):
            if num%i==0:
                divisors.append(i)
                divisors.append(num/i)
             
        return sum(divisors)==num