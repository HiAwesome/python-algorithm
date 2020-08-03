# https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode/
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False

    def insert(self, new_value):
        # if not existed, add the new element to the head
        if not self.exists(new_value):
            new_node = Node(new_value, self.head.next)
            # set the new head
            self.head.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


class MyHashSet(object):
    def __init__(self):
        self.key_range = 2069
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def __get_hash_key(self, key):
        return key % self.key_range

    def add(self, key):
        self.bucket_array[self.__get_hash_key(key)].insert(key)

    def remove(self, key):
        self.bucket_array[self.__get_hash_key(key)].delete(key)

    def contains(self, key):
        return self.bucket_array[self.__get_hash_key(key)].exists(key)
