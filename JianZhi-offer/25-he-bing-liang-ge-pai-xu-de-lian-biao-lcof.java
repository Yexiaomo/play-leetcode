/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode rst = new ListNode(0), p;
        rst.next = l1;
        p = rst;
        while(l1 != null && l2 != null){
            //对当前两个指针所指向的节点进行比大小
            if(l1.val <= l2.val){
                p.next = l1;
                l1 = l1.next;
            }else{
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        if(l1 == null){
            p.next = l2;
        }
        if(l2 == null){
            p.next = l1;
        }
        return rst.next;
    }
}
