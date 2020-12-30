if __name__ == '__main__':
    n = input()

    last, steps, width = '-', 0, 0
    for _ in range(n):
        current = raw_input()[0]

        if last == '-' and current == '.':
            width = 0
            steps += 1

        width += int(current == '.')
        if width >= 3:
            break

        last = current

    if width >= 3:
        print('N')
    else:
        print(steps)
