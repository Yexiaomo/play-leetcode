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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null)
            return new LinkedList<>();
        
        List<List<Integer>> rst = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while(!queue.isEmpty()){
            Queue<TreeNode> tmpQueue = new LinkedList<>();
            List<Integer> rowValList = new LinkedList<>();
            TreeNode tmpNode;

            while(!queue.isEmpty()){
                tmpNode = queue.remove();
                rowValList.add(tmpNode.val);
                if(tmpNode.left != null)
                    tmpQueue.add(tmpNode.left);
                if(tmpNode.right != null)
                    tmpQueue.add(tmpNode.right);
            }
            rst.add(rowValList);
            queue = tmpQueue;
        }
        return rst;
    }
}
