/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        Stack<ListNode> stack = new Stack<ListNode>();
        while(head != null){
            stack.push(head);
            head = head.next;
        }

        int[] rst = new int[stack.size()];
        int i = 0;
        while(stack.size() > 0){
            rst[i++] = stack.pop().val;
        }

        return rst;
    }
}
