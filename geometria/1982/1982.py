from math import sqrt


def convex_hull(allpoints):
    allpoints = sorted(set(allpoints))

    if len(allpoints) <= 1:
        return allpoints

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in allpoints:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(allpoints):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def distance(edgepoints):
    dist = 0.0
    for i in xrange(len(edgepoints) - 1):
        dist += sqrt((edgepoints[i][0] - edgepoints[i + 1][0]) ** 2 + (edgepoints[i][1] - edgepoints[i + 1][1]) ** 2)
    return dist


if __name__ == '__main__':
    while True:
        nPoints = input()
        if nPoints == 0:
            break
        points = []
        for i in xrange(nPoints):
            x, y = map(float, raw_input().split())
            points.append((x, y))

        convexPoints = convex_hull(points)
        convexPoints.append(convexPoints[0])
        print("Tera que comprar uma fita de tamanho %.2f." % distance(convexPoints))
