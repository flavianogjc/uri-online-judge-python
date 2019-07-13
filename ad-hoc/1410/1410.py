from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        if stdin.readline() == "0 0\n":
            break

        a = map(int, stdin.readline().split())
        b = map(int, stdin.readline().split())

        a.sort(), b.sort()
        if a[0] < b[1]:
            printf("Y\n")
        else:
            printf("N\n")