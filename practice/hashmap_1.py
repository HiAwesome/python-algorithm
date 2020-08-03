# https://leetcode-cn.com/problems/design-hashmap/solution/she-ji-ha-xi-biao-by-leetcode/
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
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
        """
        初始化数据结构
        """
        # 最好使用质数，减少碰撞
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def __get_hash_key(self, key):
        return key % self.key_space

    def put(self, key, value):
        """
        value will always be non-negative.
        :param key: int
        :param value: int
        :return: None
        """
        self.hash_table[self.__get_hash_key(key)].update(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :param key: int
        :return: int
        """
        return self.hash_table[self.__get_hash_key(key)].get(key)

    def remove(self, key):
        """
        Remove the mapping of the specified value key if this map contains a mapping for the key
        :param key: int
        :return: None
        """
        self.hash_table[self.__get_hash_key(key)].remove(key)
