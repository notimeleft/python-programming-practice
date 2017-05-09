'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        row = [1]
        res = []
        for i in range(0,numRows):
            res.append(row)
            row = self.generate_line(row)
            
            
        return res
    
    def generate_line(self,old_list):
        
        new_list = [1]
        if len(old_list)>1:
            for i in xrange(0,len(old_list)-1):
                k = old_list[i]+old_list[i+1]
                new_list.append(k)
        new_list.append(1)
        return new_list