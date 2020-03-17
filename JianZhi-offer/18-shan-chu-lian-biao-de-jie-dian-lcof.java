/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode rst = new ListNode(0), front = new ListNode(0);
        front.next = head;
        rst = front;
        while(head != null){
            if(head.val == val){
                front.next = head.next;
                break;
            }
            head = head.next;
            front = front.next;
        }
        return rst.next;
    }
}
