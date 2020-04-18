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
    public boolean isBalanced(TreeNode root) {
        //使用后序遍历辅助判断
        return PostOrderHelper(root) >= 0;
    }
    public int PostOrderHelper(TreeNode root){
        if(root == null)
            return 0;
        int leftHeight = PostOrderHelper(root.left);
        int rightHeight = PostOrderHelper(root.right);
        if(leftHeight >= 0 && rightHeight >= 0 && Math.abs(leftHeight - rightHeight) <= 1){
            return Math.max(leftHeight, rightHeight) + 1;
        }else{
            return -1;
        }
    }
}
