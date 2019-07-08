from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        try:
            N, M, K = map(int, read_line().split())

            memory = [0] * K

            for i in map(int, read_line().split()):
                memory[i % K] += 1

            soma = 0
            for i in map(int, read_line().split()):
                soma += memory[(K - (i % K)) % K]

            printf("%d\n" % soma)
        except ValueError:
            break
