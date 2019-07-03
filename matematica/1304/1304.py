from sys import stdin, stdout

read_line = stdin.readline
printf = stdout.write
if __name__ == '__main__':
    horas, minutos, segundos = 0, 0, 0
    deslocamento = 0
    speed = 0  # km/h

    while (True):
        try:
            line = read_line().split()
            Horas, Minutos, Segundos = map(int, line[0].split(':'))
            dt = (Horas * 3600 + Minutos * 60 + Segundos) - (horas * 3600 + minutos * 60 + segundos) # Em seg
            deslocamento += speed * dt

            if (len(line) == 2):
                speed = float(line[1]) / 3600.0
            else:
                printf(line[0] + ' %.2lf' % (deslocamento) + ' km\n')

            horas, minutos, segundos = Horas, Minutos, Segundos
        except:
            break