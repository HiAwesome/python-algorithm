"""
数据流中的第K大元素
https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

Python的heapq的文档：https://docs.python.org/3/library/heapq.html

1、heapq.heapify可以原地把一个list调整成堆[小顶堆] 而 heapq.nlargest 会调成大顶堆
2、heapq.heappop可以弹出堆顶，并重新调整
3、heapq.heappush可以新增元素到堆中，不会调整
4、heapq.heapreplace可以替换堆顶元素，并调整下
5、为了维持为K的大小，初始化的时候可能需要删减，后面需要做处理就是如果不满K个就新增，否则做替换；
6、heapq其实是对一个list做原地的处理，第一个元素就是最小的，直接返回就是最小的值

"""
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
