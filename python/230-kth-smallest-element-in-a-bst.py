# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #分析一波,因为是二叉搜索树,所以二叉树的中序遍历就是这个二叉树的从大到小排序

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if(root == None): return None
        #中序遍历到第k个,直接返回
        rst = None
        count = 0
        def inorderTravel(node):
            nonlocal count
            nonlocal rst
            if(count < k and node.left != None): inorderTravel(node.left)
            count += 1
            if(count == k):
                rst = node.val
                count *= 2
                return
            if(count < k and node.right != None): inorderTravel(node.right)
        inorderTravel(root)
        return rst

    #不用像上面那样定义n,rst为非局部变量
    #直接在self中定义
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.rst, self.n = 0, 0
        def inOrder(node):
            if(node == None): return
            inOrder(node.left)
            self.n += 1
            if(self.n == k):
                self.rst = node.val
                return
            inOrder(node.right)
        inOrder(root)
        return self.rst
