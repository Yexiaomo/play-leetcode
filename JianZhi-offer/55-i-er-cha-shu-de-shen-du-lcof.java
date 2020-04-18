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
    public int maxDepth(TreeNode root) {
        // if(root == null)
        //     return 0;
        // int leftDepth =1 + maxDepth(root.left);
        // int rightDepth =1 + maxDepth(root.right);
        // return (leftDepth >= rightDepth) ? leftDepth : rightDepth;
        // 整合成一段代码
        return root == null ? 0 : Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
