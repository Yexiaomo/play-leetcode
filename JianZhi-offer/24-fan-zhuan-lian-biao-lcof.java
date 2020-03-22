/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode rst = new ListNode(0);
        rst.next = null;
        ListNode tmp = null;
        while(head!=null){
            tmp = head;
            head = head.next;
            tmp.next = rst.next;
            rst.next = tmp;
        }
        return rst.next;
    }
}
