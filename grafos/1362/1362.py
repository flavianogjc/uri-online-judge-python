from sys import stdin, stdout


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    def bpm(self, u, match, seen):
        for v in range(self.jobs):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if match[v] == -1 or self.bpm(match[v], match, seen):
                    match[v] = u
                    return True
        return False

    def max_bpm(self):
        match_r = [-1] * self.jobs
        result = 0
        for j in range(self.ppl):
            seen = [False] * self.jobs
            if self.bpm(j, match_r, seen):
                result += 1
        return result


read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    etiqueta = {'XXL': 0, 'XL': 1, 'L': 2, 'M': 3, 'S': 4, 'XS': 5}
    C = input()
    for c in xrange(C):
        N, M = map(int, read_line().split())

        bpGraph = [[0] * N for i in xrange(M)]
        for m in xrange(M - 1, -1, -1):
            a, b = map(lambda x: etiqueta[str(x)], read_line().split())
            for i in xrange(N // 6):
                bpGraph[m][6 * i + a] = 1
                bpGraph[m][6 * i + b] = 1

        graph = Graph(bpGraph)

        if graph.max_bpm() >= M:
            printf('YES\n')
        else:
            printf('NO\n')
