'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #perform dfs, tracking value of node at each level. Use a dictionary to track largest value of each level. 
        self.dict={}
        self.dfs(root,0)
        res = []
        for x in self.dict.keys():
            res.append(self.dict[x])
        return res    
    def dfs(self,root,level):
        if root:
            if level in self.dict:
                if self.dict[level]<root.val:
                    self.dict[level]=root.val
            else:
                self.dict[level]=root.val
            self.dfs(root.left,level+1)
            self.dfs(root.right,level+1)