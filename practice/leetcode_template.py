from collections import deque
from typing import List


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
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]

        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]

        q = deque(zeroes_pos)
        visited = set(q)

        while q:
            i, j = q.popleft()
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    visited.add((ni, nj))

        return dist


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
