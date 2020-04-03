/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        // 使用哈希
        // 哈希表中<原表节点，新表节点>
        // 
        Map<Node,Node> map=new HashMap<>();
        Node p=head;
        while(p!=null){
            map.put(p, new Node(p.val));
            p=p.next;
        }
        p=head;
        while(p!=null){
            map.get(p).next=map.get(p.next);
            map.get(p).random=map.get(p.random);
            p=p.next;
        }
        return map.get(head);
    }
}
