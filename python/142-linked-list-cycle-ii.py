# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #用集合,判断当前链表是否存在于集合中,
        # 如果存在,则说明有环,返回当前节点
        # 如果不存在,添加到集合中
        # 结束条件为当前节点为空
        ans = set()
        while(head):
            if(head in ans):
                return head
            else:
                ans.add(head)
                head = head.next
        return None
