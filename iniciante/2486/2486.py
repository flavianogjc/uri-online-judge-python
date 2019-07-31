FOOD = {"suco": 120,
        "morango": 85,
        "mamao": 85,
        "goiaba": 70,
        "manga": 56,
        "laranja": 50,
        "brocolis": 34
        }


if __name__ == '__main__':
    while True:
        T = input()
        if T == 0:
            break

        mg = 0
        for i in xrange(T):
            line = raw_input().split()
            N = int(line[0])
            food = line[1]

            mg += N * FOOD[food]

        if mg < 110:
            print "Mais %d mg" % (110 - mg)
        elif mg <= 130:
            print mg, "mg"
        else:
            print "Menos %d mg" % (mg - 130)