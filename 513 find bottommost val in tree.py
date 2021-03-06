'''
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #perform DFS and track the level as well as the first value of each level
        self.last = root.val
        self.last_level = 0
        self.DFS(root,0)
        return self.last
    def DFS(self,root,level):   
        if root:
            if level>self.last_level:
                self.last_level = level
                self.last = root.val
            #print self.last,self.last_level
            
            self.DFS(root.left,level+1)
            self.DFS(root.right,level+1)