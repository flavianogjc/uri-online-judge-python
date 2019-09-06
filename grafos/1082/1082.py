from sys import stdin, stdout


def dfs(graph, start):
    stack = [(start, [start])]
    components = set([])
    while stack:
        vertex, path = stack.pop()
        for next in graph[vertex] - set(path):
            stack.append((next, path + [next]))
        components |= {vertex}

    return components


def components_conex(graph):
    visited = set([])
    components = []
    for v in graph:
        if v not in visited:
            new_components = dfs(graph, v)
            visited |= new_components
            components.append(list(new_components))

    return components


def good_answer(answer):
    lenght = len(answer)
    for i in xrange(0, lenght):
        answer[i].sort()
    answer.sort()

    return answer


alpha = "abcdefghijklmnopqrstuvwxyz"
scanf = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    T = input() + 1
    for case in xrange(1, T):
        V, E = map(int, scanf().split())

        graph = dict([(i, set([])) for i in alpha[0:V]])
        for _ in xrange(E):
            a, b = map(str, scanf().split())

            graph[a] |= {b}
            graph[b] |= {a}

        answer = good_answer(components_conex(graph))

        printf("Case #%d:\n" % case)
        for i in answer:
            printf(",".join(i) + ",\n")

        printf("%d connected components\n\n" % len(answer))
