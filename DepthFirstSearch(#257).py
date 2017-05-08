class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            return self.DFS([root],[],"")
        else:
            return []
    
    def DFS(self,q,res,st):
        while len(q)>0:
            k = q.pop(0)
            st+=str(k.val)+"->"
            children=0
            if k.left:
                children+=1
                q.append(k.left)
                self.DFS(q,res,st)
            if k.right:
                children+=1
                q.append(k.right)
                self.DFS(q,res,st)
            if children==0:
                res.append(st[:len(st)-2])   
            st=""
        return res    
                