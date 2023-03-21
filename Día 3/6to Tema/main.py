import circulo as c


def main():
    for r in range(1, 5):
        print('Circulo de radio {0}, tiene area {1:.2f} y circunferencia {2:.2f}'.format(
            r,
            c.area(r),
            c.circunferencia(r)
        ))


main()
