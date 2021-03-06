# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 06:40:31 2020

@author: leiya
"""
#由于在原有函数上直接写递归容易出现错误，所以最好单独写递归函数
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if root is None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root) 
        return res
    
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        stack, res = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return res


    