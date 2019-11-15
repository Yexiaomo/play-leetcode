# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
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
