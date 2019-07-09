if __name__ == '__main__':
    N = input()

    expression = raw_input()
    result = eval(expression)

    if result > N:
        print "OVERFLOW"
    else:
        print "OK"
