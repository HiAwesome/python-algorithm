from pythonds.trees.binheap import BinHeap

if __name__ == '__main__':
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)

    for i in range(4):
        print(bh.delMin())

"""
3
5
7
11
"""
