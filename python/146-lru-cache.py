from collections import OrdereDict
#使用栈表示,一指针为栈顶top,一指针为栈底bottom
class LRUCache:
    def __init__(self, capacity: int):
        #初始化栈
        self.LRUC_stack = OrdereDict()
        self.LRUC_stack_len = capacity

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        #入栈,首先判断栈是否已满
        if(len(L) >= LRUC_stack_len):
        	#找到最近最少使用的元素,替换它
        	#使用的是栈,这个最近最少使用的元素在


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)