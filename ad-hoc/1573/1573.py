from sys import stdin, stdout

scanf = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    while True:
        a, b, c = map(int, scanf().split())
        if a == 0 and b == 0 and c == 0:
            break
        else:
            sizeCub = int(pow(a * b * c, 0.3333333)).__str__() + '\n'
            printf(sizeCub)
