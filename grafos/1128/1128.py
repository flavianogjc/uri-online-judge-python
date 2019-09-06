from collections import defaultdict
from sys import stdin, stdout


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        self.components = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def scc_util(self, u, low, disc, stack_member, st):
        if self.components >= 2:
            return None
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        st.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.scc_util(v, low, disc, stack_member, st)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                low[u] = min(low[u], disc[v])

        w = -1
        # print/store connected components
        if (low[u] == disc[u]):
            while (w != u):
                w = st.pop()
                stack_member[w] = False
            self.components += 1

    def scc(self):
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stack_member = [False] * (self.V)
        st = []
        for i in range(self.V):
            if self.components >= 2:
                return None
            if disc[i] == -1:
                self.scc_util(i, low, disc, stack_member, st)


scanf = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        N, M = map(int, scanf().split())
        if N == 0 and M == 0:
            break

        graph = Graph(N)
        for i in xrange(M):
            x, y, c = map(int, scanf().split())
            graph.add_edge(x - 1, y - 1)
            if c == 2:
                graph.add_edge(y - 1, x - 1)

        graph.scc()
        if (graph.components == 1):
            printf("1\n")
        else:
            printf("0\n")
