if __name__ == '__main__':
    for _ in xrange(input()):
        arr = map(float, raw_input().split())[1:]

        med = sum(arr) / len(arr)

        best = sum([i > med for i in arr])

        print '{0:.3f}%'.format((best * 100.0) / len(arr))