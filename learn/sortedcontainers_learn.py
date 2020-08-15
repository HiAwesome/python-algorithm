"""
https://leetcode.com/discuss/general-discussion/452863/how-do-you-deal-with-no-treeset-or-treemap-in-python
Python3 可以使用 sortedcontainers 库来实现 Java 中 TreeSet, TreeMap, Collections.sort(list)
"""

from sortedcontainers import SortedList

sl = SortedList(['e', 'a', 'c', 'd', 'b'])
print(sl)  # SortedList(['a', 'b', 'c', 'd', 'e'])
sl *= 100
print(sl.count('c'))  # 100
print(sl[-3:])  # ['e', 'e', 'e']

from sortedcontainers import SortedDict

sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd)  # SortedDict({'a': 1, 'b': 2, 'c': 3})
print(sd.popitem(index=-1))  # ('c', 3)

from sortedcontainers import SortedSet

ss = SortedSet('abracadabra')
print(ss)  # SortedSet(['a', 'b', 'c', 'd', 'r'])
print(ss.bisect_left('c'))  # 2
print(ss.bisect_right('c'))  # 3
print(ss.bisect_left('f')) # 4
print(ss.bisect_right('f')) # 4