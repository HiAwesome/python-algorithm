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
        if key not in self.dict:
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key)
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    print(lru.dict)
    lru.get(1)
    print(lru.dict)
    lru.put(4, 4)
    print(lru.dict)

"""
OrderedDict([(1, 1), (2, 2), (3, 3)])
OrderedDict([(2, 2), (3, 3), (1, 1)])
OrderedDict([(3, 3), (1, 1), (4, 4)])
"""
