'''
Implement int sqrt(int x).

Compute and return the square root of x.

Subscribe to see which companies asked this question.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x==1:
            return x
        
        low = 0
        high = x
        mid = (high+low)/2
        count = 0
        
        while(mid*mid!=x):
            
            mid = (low+high)/2
            
            if high-low<2:
                if mid*mid>x:
                    return mid-1
                else:
                    return mid
            
            if mid*mid < x:
                low = mid+1
            
            else:
                high = mid
           
            
        return mid 