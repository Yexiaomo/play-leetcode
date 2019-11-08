# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None or head.next == None): return False
        slow = head
        fast = head.next
        while(fast != slow):
            if(fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    #集合判定
    def hasCycle(self, head: ListNode) -> bool:
        ans = set()
        while(head!=None):
            if(head in ans):
                return True
            else:
                ans.add(head)
                head = head.next
        return False
            