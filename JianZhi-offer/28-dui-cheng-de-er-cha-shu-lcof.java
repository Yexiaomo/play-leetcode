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
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root, root);
    }
    public boolean isSymmetric(TreeNode rootLeft, TreeNode rootRight){
        if(rootLeft == null && rootRight == null)
            return true;
        if(rootLeft == null || rootRight == null)
            return false;
        if(rootLeft.val != rootRight.val)
            return false;
        return isSymmetric(rootLeft.left, rootRight.right) && isSymmetric(rootLeft.right, rootRight.left);
    }
}
