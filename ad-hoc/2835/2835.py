if __name__ == '__main__':
    n = input()
    arr = [0] + map(int, raw_input().split())
    arr.sort()

    its_possible = True
    for i in xrange(n):
        if arr[i + 1] - arr[i] > 8:
            its_possible = False
            break

    print('S' if its_possible else 'N')
