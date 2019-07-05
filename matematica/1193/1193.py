if __name__=='__main__':
    n = input()
    for i in xrange(1, n+1):
        num, base = raw_input().split()

        print("Case %d:" % i)
        if(base=='bin'):
            num = int(num, 2)
            print("%d dec" % num )
            print("%s hex\n" % hex(num)[2:])
        elif(base=='dec'):
            num = int(num)
            print("%s hex" % hex(num)[2:])
            print ("%s bin\n" % bin(num)[2:])
        else:
            num = int(num, 16)
            print("%d dec" % num)
            print ("%s bin\n" % bin(num)[2:])
