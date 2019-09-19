from bisect import bisect_left


def can_split(i):
    global arr, med

    item = (arr[i - 1] if i else 0) + med

    return (item <= arr[-1]) and (arr[bisect_left(arr, item)] == item)


def find_ge(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return i

    return


def maior(i):
    global arr, med

    item = (arr[i - 1] if i else 0) + med

    return find_ge(arr, item)


def solve():
    global med
    if arr[-1] % 2 == 1:
        return 'N'
    else:
        med = arr[-1] // 2
        for i in xrange(n):
            if can_split(i):
                m = maior(i)
                for j in xrange(i + 1, m):
                    if can_split(j):
                        return 'Y'
    return 'N'


med = None
if __name__ == '__main__':
    n = input()
    arr = map(int, raw_input().split())

    for i in xrange(1, n):
        arr[i] += arr[i - 1]

    print solve()
