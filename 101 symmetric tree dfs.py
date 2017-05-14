'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    #simply traverse the tree twice: once to get a list of elements from DFS, another to get a list from reverse DFS. 
    #Return true if the two traversals returned the same list, false otherwise. 
        return self.DFS(root,[])==self.reverseDFS(root,[])
    
    
    def DFS(self,root,results):
        if root:
            results.append(root.val)
            if root.left:
                self.DFS(root.left,results)
            else:
                results.append(None)
            if root.right:
                self.DFS(root.right,results)
            else:
                results.append(None)
        return results        
    
    def reverseDFS(self,root,results):
        if root:
            results.append(root.val)
            if root.right:
                self.reverseDFS(root.right,results)
            else:
                results.append(None)
            if root.left:
                self.reverseDFS(root.left,results)
            else:
                results.append(None)
        return results        