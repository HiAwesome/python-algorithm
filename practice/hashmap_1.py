"""
设计哈希表
https://leetcode-cn.com/problems/design-hashmap/
"""


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def put(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):
    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def __get_hash_key(self, key):
        return key % self.key_space

    def put(self, key, value):
        self.hash_table[self.__get_hash_key(key)].put(key, value)

    def get(self, key):
        return self.hash_table[self.__get_hash_key(key)].get(key)

    def remove(self, key):
        self.hash_table[self.__get_hash_key(key)].remove(key)
