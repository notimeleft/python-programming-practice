'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return min(self.dfs(root,1,[]))
    def dfs(self,root,minpath,res):    
        
        if root.left:
            self.dfs(root.left,minpath+1,res)
        if root.right:
            self.dfs(root.right,minpath+1,res)
        if not root.left and not root.right:
            res.append(minpath)
            
        return res        