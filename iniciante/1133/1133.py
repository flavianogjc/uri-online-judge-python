if __name__ == '__main__':
    a = input()
    b = input()

    if a > b:
        a, b = b, a

    for i in xrange(a + 1, b):
        if i % 5 == 2 or i % 5 == 3:
            print(i)