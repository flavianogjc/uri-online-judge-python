if __name__ == '__main__':
    NC = input()
    case = 1

    for j in range(NC):
        n, k = map(int, raw_input().split())  # Pessoas, salto

        N, m = n, range(1, n + 1)
        stop = 0

        for i in range(1, N):
            n = len(m)
            stop = (stop + k - 1) % n
            del m[stop]

        print("Case " + case.__str__() + ": " + m[0].__str__())
        case += 1
