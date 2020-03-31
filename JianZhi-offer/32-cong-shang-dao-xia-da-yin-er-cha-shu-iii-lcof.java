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
        List<List<Integer>> rst = new LinkedList<>();
        if(root == null)
            return rst;
        
        Queue<TreeNode> queueRowNode = new LinkedList<>();
        boolean flag = true;
        queueRowNode.add(root);

        while(!queueRowNode.isEmpty()){
            LinkedList<Integer> tmpRowVal = new LinkedList<>();
            Queue<TreeNode> tmpRowNode = new LinkedList<>();
            while(!queueRowNode.isEmpty()){
                TreeNode tmpNode = queueRowNode.remove();
                if(flag){
                    tmpRowVal.add(tmpNode.val);
                }else{
                    tmpRowVal.addFirst(tmpNode.val);
                }

                if(tmpNode.left != null)
                    tmpRowNode.add(tmpNode.left);
                if(tmpNode.right != null)
                    tmpRowNode.add(tmpNode.right);
            }
            flag=!flag;
            queueRowNode = tmpRowNode;
            rst.add(tmpRowVal);
        }
        return rst;        
    }
}
