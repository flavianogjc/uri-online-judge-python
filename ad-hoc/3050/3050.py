if __name__ == '__main__':
    n = input()
    arr = map(int, raw_input().split())
    a, b, j = 0, 1, 0
    d = b - a + arr[a] + arr[b]

    for i in xrange(2, n):
        if arr[a] + i - a <= arr[i]:
            j = i
        if i - j + arr[i] + arr[j] >= d:
            a, b = j, i
            d = i - j + arr[i] + arr[j]

    print d
