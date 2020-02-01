'''
我的思考,
实际的数据存储在一个字典中
再实现一个栈,栈顶存储是最近访问的元素,这样栈顶永远就是需要被置换的
'''


#第一种方法
#利用OrderedDict库函数,参考官方题解
from collections import OrderedDict
class LRUCache(OrderedDict):
    
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if(key not in self): return -1
        #这一步就是将当前访问的key,移动至顶部,意思差不多
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if(key in self):
            self.move_to_end(key)
        self[key] = value
        #如果超出
        if(len(self) > self.capacity):
            #popitem()移除并返回一个(key, value)键值对。
            #如果 last 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。
            self.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)