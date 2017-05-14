'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = [1]
        for x in xrange(0,rowIndex):
         k = self.generate(k)
        return k 
         
    
    def generate(self,k):
        newlist = []
        newlist.append(1)
        for i in xrange(0,len(k)-1):
            current = k[i]
            nxt = k[i+1]
            newlist.append(current+nxt)
        newlist.append(1)
        return newlist