"""
https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/python3er-cha-sou-suo-shu-shu-ju-liu-zhong-de-di-k/
https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/703-pythonshi-xian-shu-ju-liu-zhong-di-kda-xiao-di/

Python的heapq的文档：https://docs.python.org/3/library/heapq.html

1、heapq.heapify可以原地把一个list调整成堆[小顶堆] 而 heapq.nlargest 会调成大顶堆
2、heapq.heappop可以弹出堆顶，并重新调整
3、heapq.heappush可以新增元素到堆中，不会调整
4、heapq.heapreplace可以替换堆顶元素，并调整下
5、为了维持为K的大小，初始化的时候可能需要删减，后面需要做处理就是如果不满K个就新增，否则做替换；
6、heapq其实是对一个list做原地的处理，第一个元素就是最小的，直接返回就是最小的值

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        self.kLarge = None  # 记录第k大
        for i in nums:
            # 若根节点为空，或者根节点的count<k直接插入
            if not self.root or self.root.count < k:
                self.root = self.insertIntoBST(self.root, i)
            else:  # 当前二叉搜索树的元素数>=k
                if not self.kLarge:  # 计算第k大
                    self.kLarge = self.findKHelper(self.root, k).val
                if i > self.kLarge:  # 如果当前值大于第k大，插入并重新寻找第k大
                    self.root = self.insertIntoBST(self.root, i)
                    self.kLarge = self.findKHelper(self.root, k).val

    def add(self, val: int) -> int:
        # self.kLarge没有值，或者当前值大于self.kLarge才插入
        if self.kLarge and val > self.kLarge or not self.kLarge:
            self.root = self.insertIntoBST(self.root, val)
        self.kLarge = self.findKHelper(self.root, self.k).val
        return self.kLarge

    def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
        if not cur:  # 首次插入元素
            cur = TreeNode(val)
            return cur
        if cur.val < val:  # 插入元素比当前元素大，插入至右子树
            cur.right = self.insertIntoBST(cur.right, val)
        else:  # 插入元素比当前元素小或等于，插入至左子树
            cur.left = self.insertIntoBST(cur.left, val)
        cur.count += 1  # 若插入至子树，当前节点的count需要+1
        return cur

    def findKHelper(self, cur: TreeNode, k) -> TreeNode:
        curCnt = 1  # 如果无右节点，当前是第1大的数
        if cur.right:  # 如果有右节点，则当前是cur.right.count+1大的数
            curCnt += cur.right.count
        if k == curCnt:  # 当前值即为第k大
            return cur
        elif k < curCnt:  # 第k大在右子树
            return self.findKHelper(cur.right, k)
        else:  # 第k大在左子树，为左子树的第k-curCnt大
            return self.findKHelper(cur.left, k - curCnt)


import heapq


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
