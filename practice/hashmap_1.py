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
            if kv[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class MyHashMap(object):
    def __init__(self):
        self.bucket_size = 2069
        self.hashmap = [Bucket() for _ in range(self.bucket_size)]

    def __get_hash_key(self, key):
        return key % self.bucket_size

    def put(self, key, value):
        self.hashmap[self.__get_hash_key(key)].put(key, value)

    def get(self, key):
        return self.hashmap[self.__get_hash_key(key)].get(key)

    def remove(self, key):
        self.hashmap[self.__get_hash_key(key)].remove(key)
