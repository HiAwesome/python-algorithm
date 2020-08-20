import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def myAtoi(self, str: str) -> int:
        return 100


class TestSolution(unittest.TestCase):
    method = Solution().myAtoi

    def test_1(self):
        self.assertEqual(self.method('42'), 42)

    def test_2(self):
        self.assertEqual(self.method('   -42'), -42)

    def test_3(self):
        self.assertEqual(self.method('4193 with words'), 4193)

    def test_4(self):
        self.assertEqual(self.method('words and 987'), 0)

    def test_5(self):
        self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
