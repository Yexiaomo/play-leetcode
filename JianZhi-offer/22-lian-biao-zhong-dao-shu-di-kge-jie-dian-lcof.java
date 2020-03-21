/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    //双指针, 两个指针距离相差为k-1
    public ListNode getKthFromEnd(ListNode head, int k) {
        if(head == null || k < 1)
            return null;

        ListNode fast = head, slow = null;
        int i = 1;
        while(fast != null && i < k){
            fast = fast.next;
            i++;
        }
        
        if(i < k || fast==null){
            return slow;
        }
        slow = head;
        while(fast.next!=null){
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}
