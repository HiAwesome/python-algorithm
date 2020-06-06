"""
LRU Cache 的实现
https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/
为什么Python 3.6以后字典有序并且效率更高？
https://www.cnblogs.com/xieqiankun/p/python_dict.html
但还是依然要使用 OrderedDict，因为 popitem 接受参数 last，而默认的 Dict 不接受
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, size):
        self.size = size
        self.dict = OrderedDict()

    def set(self, key, value):
        self.dict[key] = value
        self.dict.move_to_end(key)
        if len(self.dict) > self.size:
            self.dict.popitem(last=False)

    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    print(lru.dict)
    lru.get(1)
    print(lru.dict)
    lru.set(4, 4)
    print(lru.dict)

"""
OrderedDict([(1, 1), (2, 2), (3, 3)])
OrderedDict([(2, 2), (3, 3), (1, 1)])
OrderedDict([(3, 3), (1, 1), (4, 4)])
"""
