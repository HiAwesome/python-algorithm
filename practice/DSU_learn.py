class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def get_root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def in_connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        self.parent[p_root] = q_root
