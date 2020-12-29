from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    is_body, html = False, ''
    while True:
        line_code = read_line()
        if '<body>' in line_code:
            is_body = True
            continue
        
        if '</body>' in line_code:
            break
        
        if is_body:
            html += line_code

    printf(html)
