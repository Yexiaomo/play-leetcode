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
    //思路按照树的先序遍历走
    public TreeNode mirrorTree(TreeNode root) {
        /*虽然这么写代码看起来繁多, 但思路很清晰
          后面的三个else可以合并, 合并后代码在下面
        */
        if(root == null){
            return root;
        }else if(root.left == null){
            root.left = root.right;
            root.right = null;
            mirrorTree(root.left);
        }else if(root.right == null){
            root.right = root.left;
            root.left = null;
            mirrorTree(root.right);
        }else{
            TreeNode tmp = root.left;
            root.left = root.right;
            root.right = tmp;
            mirrorTree(root.left);
            mirrorTree(root.right);
        }
        return root;
    }
    public TreeNode mirrorTree(TreeNode root){
        if(root == null)
            return null;
        TreeNode tmp = root.left;
        root.left = mirrorTree(root.right);
        root.right = mirrorTree(tmp);
        return root;
    }
}
