# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #递归处理
        if root in {p,q,None}: #如果二叉树的根节点是p,q,None三者其中的一种,则返回root: 1.p或者q是root,则两者的最近公共祖先是root 2.root是空的,即二叉树是空树,返回None,也是返回root
            return root
        left=self.lowestCommonAncestor(root.left,p,q) #去左子树看是否可以访问到p或q,并把结果返回给left
        right=self.lowestCommonAncestor(root.right,p,q) #去右子树看是否可以访问到p或q,并把结果返回给right
        return root if left and right else left or right #如果left,right都不为空,则说明在左子树和右子树都分别访问到了p或q,则此时root是最近公共祖先,否则,哪个不空则返回哪个
   
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root in [None, p, q]): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return right if(left == None) else left if(right == None) else root
