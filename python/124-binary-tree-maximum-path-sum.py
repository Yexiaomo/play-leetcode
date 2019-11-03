# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         if(not root): return 0
#         rst = []
#         def dfs(childNode):
#             parentNode = childNode.val
#             if(childNode.left and childNode.right):
#                 plNode = parentNode + dfs(childNode.left)
#                 prNode = parentNode + dfs(childNode.right)
#                 tmp = max(max(parentNode, plNode+prNode-parentNode), max(plNode, prNode))
#             elif(childNode.left):
#                 plNode = parentNode + dfs(childNode.left)
#                 tmp = max(parentNode, plNode)
#             elif(childNode.right):
#                 prNode = parentNode + dfs(childNode.right)
#                 tmp = max(parentNode, prNode)
#             else:
#                 tmp = parentNode
#             rst.append(tmp)
#             return tmp
#         dfs(root)
#         print(rst)
#         return max(rst)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if(not root): return 0
        rst = -9999999
        def fun(childNode):
            nonlocal rst
            if(not childNode): return 0
            #如果为负直接舍去当前节点的子节点
            left = max(0, fun(childNode.left))
            right = max(0, fun(childNode.right))
            rst = max(rst, childNode.val+left+right)
            return max(left, right)+childNode.val
        fun(root)
        return rst