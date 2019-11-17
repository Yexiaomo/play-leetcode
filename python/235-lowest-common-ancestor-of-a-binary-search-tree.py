# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	#思路1:根据二叉搜索的性质, 当前值节点值和p,q节点的值进行比较
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(p.val >= q.val):
            max = p.val
            min = q.val
        else:
            max = q.val
            min = p.val
        while(root):
            if(root.val > max):
                root = root.left
            elif(root.val < min):
                root = root.right
            else:
                return root
        return