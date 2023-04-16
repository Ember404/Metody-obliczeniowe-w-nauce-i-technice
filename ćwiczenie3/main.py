import numpy as np
from matplotlib import pyplot
from math import pi
from math import sin, cos



def funkcja(x):
    return x * sin((pi * 4) / x)

def max_blad(x, y):
    blad = 0
    for i in range(len(x)):
        diff = y[i] - funkcja(x[i])
        if blad < abs(diff):
            blad = abs(diff)
    return blad

def pochodna(x):
    return sin((pi * 4) / x) - (4 * pi * cos((pi * 4) / x)) / x


def druga_pochodna(x):
    return -(4 * (pi ** 2) * sin((pi * 4) / x)) / (x ** 3)


def s(x, xn, yn, h, w):
    i =(int) ((x-0.25) // h)
    if i >= (len(xn)-1):
        return 0
    b = (yn[i + 1] - yn[i]) / h - h * (w[i+1] + 2 * w[i])
    c = 3 * w[i]
    d = (w[i + 1] - w[i]) / h

    return yn[i] + b * (x - xn[i]) + c * (x - xn[i]) ** 2 + d * (x - xn[i]) ** 3


if __name__ == '__main__':
    n = int(input("Podaj liczbe wezlow (liczba wezlow + 1 = liczba przedzialow):\n"))
    cubic_or_square = input("Ktorego stopnia ma być spline? (2 albo 3)\n")
    warunki= input("Jakie warunki brzegowe? (2- znana druga pochodna, default- warunki z wykładu)\n")

    xn = np.linspace(0.25, 0.8, n)
    yn = [funkcja(xn[i]) for i in range(n)]
    h = (0.8 - 0.25) / (n - 1)

    R = np.array([0.0 for _ in range(n)])
    L = np.array([[0.0 for i in range(n)] for j in range(n)])

    if int(cubic_or_square)==3:
        title="Interpolacja funkcją 3 stopnia, przedziały: "+str(n-1)

        if warunki == "2":
            #warunki brzegowe- określona druga pochodna
            R[0] = druga_pochodna(0.25) / 6
            L[0, 0] = 1
            R[-1] = druga_pochodna(0.8) / 6
            L[-1, -1] = 1

        else:
            # warunki brzegowe z wykładu
            L[0, 0] = h * -1
            L[0, 1] = h
            L[-1, -1] = h * -1
            L[-1, -2] = h
            R[0] = h ** 2 * ((yn[1] - yn[0]) / h) ** 3
            R[-1] = -h * ((yn[-2] - yn[-3]) / h) ** 3

        #wypełnianie macierzy
        for i in range(1, n - 1):
            L[i, i - 1] = h
            L[i, i] = 4 * h
            L[i, i + 1] = h

        for i in range(1, n - 1):
            R[i] = (yn[i+1]-yn[i]-yn[i]+yn[i-1])/h

    else:
        title = "Interpolacja funkcją 2 stopnia, przedziały: " + str(n - 1)

        # warunki brzegowe- określona pierwsza pochodna
        R[0] = pochodna(0.25)
        L[0, 0] = 1
        R[-1] = pochodna(0.8)
        L[-1, -1] = 1

        for i in range(1, n - 1):
            L[i, i - 1] = 1 - h/2
            L[i, i] = h/2
            L[i, i + 1] = -1

        for i in range(1, n - 1):
            R[i] = (yn[i-1]-yn[i+1])/h


    w = np.linalg.solve(L, R)
    #print("L:", L, "\n\nR:", R, "\n\nw:", w)

    # wizualizacja
    x = np.linspace(0.25, 0.8, 100)
    y = [funkcja(x[i]) for i in range(100)]
    spline = [s(x[i], xn, yn, h, w) for i in range(100)]
    spline[-1] = yn[-1]
    print(max_blad(x,spline))

    pyplot.plot(x, y, color="pink")
    pyplot.scatter(xn,yn,color="red")
    pyplot.plot(x,spline,color="blue")
    pyplot.title(title)
    pyplot.show()
