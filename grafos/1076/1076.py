def dfs(graph, start):
    stack = [(start, [start])]
    soma = 0
    while stack:
        vertex, path = stack.pop()
        for next in graph[vertex] - set(path):
            soma += 1
            stack.append((next, path + [next]))
    return soma


if __name__ == '__main__':
    T = input()
    for i in xrange(T):
        start = input()

        V, A = map(int, raw_input().split())

        graph = dict([(i, set([])) for i in xrange(V)])
        for j in xrange(A):
            a, b = map(int, raw_input().split())

            graph[a] |= set([b])
            graph[b] |= set([a])

        print(dfs(graph, start) << 1)
