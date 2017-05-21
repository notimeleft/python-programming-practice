'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''

from math import sqrt
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        k = set()
        
        k.add(''.join(str(i) for i in p1))
        k.add(''.join(str(i) for i in p2))
        k.add(''.join(str(i) for i in p3))
        k.add(''.join(str(i) for i in p4))
        if len(k)<4:
            return False
        res = []
        res.append(self.distance_two_pts(p1,p2))
        res.append(self.distance_two_pts(p3,p2))
        res.append(self.distance_two_pts(p3,p4))
        res.append(self.distance_two_pts(p1,p4))
        res.append(self.distance_two_pts(p3,p1))
        res.append(self.distance_two_pts(p2,p4))
        res.sort()
        print res
        if res[4]==res[5]:
            if res[0]==res[1] and res[1]==res[2] and res[2]==res[3]:
                return True
            else:
                return False
        return False        
        
        
    def distance_two_pts(self,x,y):
        x1 = x[0]
        y1 = x[1]
        
        x2 = y[0]
        y2 = y[1]
        
        k = abs(x1-x2)
        j = abs(y1-y2)
        
        return sqrt(k*k+j*j)
        