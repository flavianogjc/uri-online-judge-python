from sys import stdin, stdout


def solver(train):
    station, pointer = [], 0
    for i in xrange(1, N + 1):
        station.append(i)
        while station and station[-1] == train[pointer]:
            pointer += 1
            station.pop()
    if station:
        printf("No\n")
    else:
        printf("Yes\n")


read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        N = int(stdin.readline())
        if N == 0:
            break

        while True:
            trem = map(int, read_line().split())
            if trem[0] == 0:
                printf("\n")
                break
            else:
                solver(trem)
