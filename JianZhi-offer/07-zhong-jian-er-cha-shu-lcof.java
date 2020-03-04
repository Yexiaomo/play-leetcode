/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        //递归结束条件
        if(preorder.length < 1) return null;
        int rootVal = preorder[0], rootIndex = 0;
        //寻找当前root节点
        for(int _val : inorder){
            if(_val == rootVal) break;
            ++rootIndex;
        }
        TreeNode root = new TreeNode(rootVal);
        //进行递归
        root.left = buildTree(Arrays.copyOfRange(preorder, 1, rootIndex+1), Arrays.copyOfRange(inorder, 0, rootIndex));
        root.right = buildTree(Arrays.copyOfRange(preorder, rootIndex+1, preorder.length), Arrays.copyOfRange(inorder, rootIndex+1, preorder.length));
        return root;
    }
}
