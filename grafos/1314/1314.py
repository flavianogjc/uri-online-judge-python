from collections import defaultdict
from sys import stdin, stdout, setrecursionlimit


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.bridges = []
        self.parent = None
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, low, disc):
        children = 0

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        for v in self.graph[u]:
            if not visited[v]:
                self.parent[v] = u
                children += 1
                self.bridge_util(v, visited, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    self.bridges.append((u, v))
            elif v != self.parent[u]:
                low[u] = min(low[u], disc[v])

    def find_parent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def joint(self, u, v, rank):
        x, y = self.find_parent(u), self.find_parent(v)
        if x == y:
            return None

        if rank[x] > rank[y]:
            rank[x] += rank[y]
            self.parent[y] = x
        else:
            rank[y] += rank[x]
            self.parent[x] = y

    def bridge(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        self.parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, low, disc)

        self.parent = range(self.V)
        rank = [0] * self.V
        for u, v in self.bridges:
            self.joint(u, v, rank)


if __name__ == '__main__':
    setrecursionlimit(10 ** 5) # Increasing recursion limit

    while True:
        N, M, C = map(int, stdin.readline().split())
        if N == 0 and M == 0 and C == 0:
            break

        graph = Graph(N)
        while M:
            u, v = map(lambda x: int(x) - 1, stdin.readline().split())
            graph.add_edge(u, v)
            M -= 1

        graph.bridge()
        while C:
            u, v = map(lambda x: int(x) - 1, stdin.readline().split())
            if graph.find_parent(u) == graph.find_parent(v):
                stdout.write("Y\n")
            else:
                stdout.write("N\n")
            C -= 1

        stdout.write("-\n")