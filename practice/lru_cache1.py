"""
LRU Cache
https://leetcode-cn.com/problems/lru-cache/

为什么Python 3.6以后字典有序并且效率更高？
https://www.cnblogs.com/xieqiankun/p/python_dict.html
但还是依然要使用 OrderedDict，因为 popitem 接受参数 last，而默认的 Dict 不接受
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last=False)

        self.dict[key] = value
        self.dict.move_to_end(key)
