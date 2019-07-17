if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        n = input()
        sets = tuple([set(map(int, raw_input().split())[1::]) for j in xrange(n)])
        n = input()
        for j in xrange(n):
            op, s1, s2 = map(lambda x: int(x) - 1, raw_input().split())
            if op == 0:
                print(len(sets[s1] & sets[s2]))
            elif op == 1:
                print(len(sets[s1] | sets[s2]))
