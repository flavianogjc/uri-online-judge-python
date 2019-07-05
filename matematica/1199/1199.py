if __name__=='__main__':
    while(True):
        num = raw_input()

        if('-' in num):
            break
        elif('0x' in num):
            num = int(num[2:], 16)
            print(num)
        else:
            num = int(num)
            print('0x'+hex(num).upper()[2:])