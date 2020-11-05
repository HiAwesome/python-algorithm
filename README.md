# [用 Python 解决数据结构与算法问题](https://book.douban.com/subject/21325184//)

## 递归三大定律

1. 递归算法必须有个基本结束条件。
2. 递归算法必须改变自己的状态并向基本结束条件演进。
3. 递归算法必须递归地调用自身。

## 二分查找需要有序列表

即使二分搜索通常比顺序搜索要好，值得注意的是，对于较小的n值，排序所附加的消耗可能是不值得的。\
事实上，我们应当一直考虑进行额外的排序工作来得到搜索优势是否是有效开销。\
如果我们可以排序一次然后搜索许多次，排序开销并不那么显著。\
然而，对于大列表，哪怕是一次排序的消耗也可能是巨大的，从一开始简单执行顺序搜索也许是最好的选择。

## 元组和列表的效率差异

参考 [Are tuples more efficient than lists in Python?](https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python) 和 [Why is tuple faster than list in Python?](https://stackoverflow.com/questions/3340539/why-is-tuple-faster-than-list-in-python) 得出结论： 
元组的性能往往比几乎每个类别中的列表都要好：

1. 元组可以恒定折叠。
2. 元组可以重复使用而不是复制。
3. 元组是紧凑的，并且不会过度分配。
4. 元组直接引用其元素。

## AVL树搜索

这个推导告诉我们，在任何时候，我们的AVL树的高度等于树中节点数目的对数的常数（1.44）倍。\ 
这是搜索我们的AVL树的好消息，因为它将搜索限制为 O(logN)。
