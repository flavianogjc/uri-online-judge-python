from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    if "zelda" in read_line().lower():
        printf("Link Bolado\n")
    else:
        printf("Link Tranquilo\n")
