if __name__ == '__main__':
    B, E = input(), input()

    resp = pow(B, E, 9)  # B**E mod 9
    if (resp):
        print(resp)
    else:
        print(9)