if __name__ == '__main__':
    am, rm, em = map(int, raw_input().split())
    av, rv, ev = map(int, raw_input().split())
    size_str = len(raw_input())

    m = 2 * am + rm + em * size_str
    v = 2 * av + rv + ev * size_str

    if m < v:
        print("Matheus")
    elif v < m:
        print("Vinicius")
    else:
        print("Empate")
