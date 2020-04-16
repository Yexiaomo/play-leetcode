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
    //二叉搜索树,先右->中->左就是从大到小遍历
    private int k;
    private int rst;

    public int kthLargest(TreeNode root, int k) {
        this.k = k;
        this.rst = 0;
        HelperOrder(root);
        return rst;
    }

    public void HelperOrder(TreeNode root){
        if(root == null || k <= 0)
            return;
        HelperOrder(root.right);
        k--;
        if(k == 0){
            rst = root.val;
            return;
        }
        HelperOrder(root.left);
    }
}
