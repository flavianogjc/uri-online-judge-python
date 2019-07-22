from sys import stdin, stdout


def dijkstra(graph, source, dest):
    vertices = set(sum(([i[0], i[1]] for i in graph), []))

    dist = {vertex: inf for vertex in vertices}
    previous = {vertex: None for vertex in vertices}
    dist[source] = 0

    next = {vertex: set([]) for vertex in vertices}
    for start, end, cost in graph:
        next[start].add((end, cost))

    Q = vertices
    while Q:
        u = min(Q, key=lambda vertex: dist[vertex])
        Q.remove(u)
        if dist[u] == inf or u == dest:
            break
        for v, cost in next[u]:
            aux = dist[u] + cost
            if aux < dist[v]:
                dist[v] = aux
                previous[v] = u

    route, u = [], dest
    while previous[u]:
        route = [u] + route
        u = previous[u]
    route = [u] + route

    return route, dist[dest]


inf = float('inf')
if __name__ == '__main__':
    while True:
        C, E = map(int, stdin.readline().split())
        if C == 0 and E == 0:
            break

        graph = []
        while E:
            x, y, c = map(int, stdin.readline().split())
            graph.append([x, y, c])
            graph.append([y, x, c])
            E -= 1

        init = int(stdin.readline())

        path, time = dijkstra(graph, init, 1)

        if time <= 120:
            stdout.write("Will not be late. Travel time - " + str(time) + " - best way -")
            for p in path:
                stdout.write(" " + str(p))
            stdout.write("\n")
        else:
            stdout.write(
                "It will be " + str(time - 120) + " minutes late. Travel time - " + str(time) + " - best way -")
            for p in path:
                stdout.write(" " + str(p))
            stdout.write("\n")
