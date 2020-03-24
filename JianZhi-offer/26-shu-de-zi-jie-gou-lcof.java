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
    public boolean isSubStructure(TreeNode A, TreeNode B) {
        //初步思路: 通过先序遍历,找到A中节点和B根节点相同的
        //找到后, 再一次判断后面的节点
        boolean rst = false;
        if(A != null && B != null){
            if(A.val == B.val)
                rst = DoesIsSubStructure(A, B);
            if(!rst)
                rst = isSubStructure(A.left, B);
            if(!rst)
                rst = isSubStructure(A.right, B);
        }
        return rst;
    }
    public boolean DoesIsSubStructure(TreeNode A, TreeNode B){
        if(B == null)
            return true;
        if(A == null)
            return false;
        if(A.val != B.val)
            return false;
        return DoesIsSubStructure(A.left, B.left) && DoesIsSubStructure(A.right, B.right);
    }
}
