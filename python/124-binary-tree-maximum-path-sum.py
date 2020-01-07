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
        #将结果初始为最小值
        #这里也可以写成self.result = float("-inf") = 负无穷
        self.result = -sys.maxsize-1
        def fun(node):
            if(not node): return 0
            #如果为负直接舍去当前节点的子节点
            left = max(0, fun(node.left))
            right = max(0, fun(node.right))
            self.result = max(self.result, node.val+left+right)
            return max(left, right) + node.val
        fun(root)
        return self.result
