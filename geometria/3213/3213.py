if __name__ == '__main__':
    k = input()
    while k != 0:
        archs = map(float, raw_input().split())
        archs.sort()

        s = 0
        flag = False
        for i in range(len(archs) - 1):
            s += archs[i]
            if s >= archs[i + 1]:
                flag = True
                break

        print('YES' if flag else 'NO')

        k = input()
