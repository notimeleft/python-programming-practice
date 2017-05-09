
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            return 1 in self.dfs(root,[root],[],"",sum,[])
        return False    
    def dfs(self,root,q,paths,single_path,target,results):
        
        if(len(q)>0):
            k = q.pop(0)
            
            single_path+=str(k.val)+","
            if k.left:
                q.append(k.left)
                self.dfs(k.left,q,paths,single_path,target,results)
            if k.right:
                q.append(k.right)
                self.dfs(k.right,q,paths,single_path,target,results)
            if not k.left and not k.right:
                #print single_path
                if self.check_sum(single_path,target):
                    results.append(1)
                paths.append(single_path[:len(single_path)-1])
                single_path=""
        return results
        #return False
        
    def check_sum(self,single_path,target):
        f = single_path[:len(single_path)-1].split(",")
        f = map(int,f)
        print sum(f),target
        return sum(f)==target