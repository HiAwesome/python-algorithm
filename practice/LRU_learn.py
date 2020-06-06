"""
LRU Cache 的实现
https://www.jianshu.com/p/e41ec08e4aa6
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
        if key in self.dict:
            self.dict.pop(key)
        if self.size == len(self.dict):
            self.dict.popitem(last=False)
        self.dict.update({key: value})

    def get(self, key):
        if key in self.dict:
            value = self.dict.pop(key)
            self.dict.update({key: value})
        else:
            value = -1

        return value


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    print(lru.dict)
    lru.get(100)
    print(lru.dict)
    lru.set(4, 4)
    print(lru.dict)

"""
OrderedDict([(1, 1), (2, 2), (3, 3)])
OrderedDict([(1, 1), (2, 2), (3, 3)])
OrderedDict([(2, 2), (3, 3), (4, 4)])
"""
