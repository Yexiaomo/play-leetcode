/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    Node head = null, tail = null, pre = null;
    public Node treeToDoublyList(Node root) {
        if(root == null)
            return root;
        inOrder(root);
        head.left = tail;
        tail.right = head;
        return head;
    }
    public void inOrder(Node root){
        if(root == null)
            return;
        
        inOrder(root.left);
        if(pre == null){
            head = root;
        }else{
            pre.right = root;
        }
        
        root.left = pre;
        pre = root;
        tail = root;
        
        inOrder(root.right);
        return;
    }
}
