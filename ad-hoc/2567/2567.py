if __name__ == '__main__':
    while True:
        try:
            n = input()
            num = map(int, raw_input().split())

            letalide = 0
            num.sort()
            i, j = 0, n - 1
            n = (n - 1) / 2
            while i <= n:
                letalide += num[j] - num[i]
                i += 1
                j -= 1

            print(letalide)
        except:
            break
