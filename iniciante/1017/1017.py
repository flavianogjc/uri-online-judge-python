if __name__ == '__main__':
    dt = input()  # Horas
    speed = input()  # Km/h

    print("%.3lf" % (speed * dt / 12.00))
