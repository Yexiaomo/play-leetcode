# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        def fun(subNode):
            if(not subNode): return 0
            nleft = fun(subNode.left)
            nright = fun(subNode.right)
            return 1+max(nleft,nright)
        return fun(root)
        '''
        #上面的代码简写版
        if(not root): return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    #最大深度,也就是二叉树的层数
    #尝试层序遍历
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None): return 0
        depth, queue = 0, [root]
        while(queue != []):
            depth += 1
            count = len(queue)
            for i in range(count):
                node = queue.pop(0)
                if(node.left != None): queue.append(node.left)
                if(node.right != None): queue.append(node.right)
        return depth
