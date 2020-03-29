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
    public int[] levelOrder(TreeNode root) {
        if(root == null)
            return new int[0];
        Queue<TreeNode> queue = new LinkedList();
        int[] rst = new int[1024];
        int i = 0;
        queue.add(root);
        TreeNode tmp = null;
        while(!queue.isEmpty()){
            tmp = queue.remove();
            rst[i++] = tmp.val;
            if(tmp.left != null)
                queue.add(tmp.left);
            if(tmp.right != null)
                queue.add(tmp.right);
        }
        return Arrays.copyOf(rst, i);
    }
}
