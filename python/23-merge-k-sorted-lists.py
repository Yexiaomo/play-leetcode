# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        rst = ListNode(0)
        p = rst
        cnt_None = 0
        for l in lists:
            if(l == None):
                cnt_None += 1
        for i in range(cnt_None):
            lists.remove(None)
        while(len(lists) > 0):
            min = 0
            for i in range(1, len(lists)):
                if(lists[i].val < lists[min].val):
                    min = i
            p.next = lists[min]
            
            if(lists[min].next != None):
                lists[min] = lists[min].next    
            else:
                lists.pop(min)
            p = p.next
        return rst.next