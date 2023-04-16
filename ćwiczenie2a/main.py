from matplotlib import pyplot as plt
from matplotlib import axis
from numpy import linspace
from numpy import copy
from math import pi
from math import sin, cos
from numpy import array
from numpy import where


def funkcja(x):
    return x * sin((pi * 4) / x)


def Lk(x, k, xn):
    iloczyn = 0
    for i in range(len(xn)):
        if i != k:
            if iloczyn == 0:
                iloczyn = (x - xn[i]) / (xn[k] - xn[i])
            else:
                iloczyn *= (x - xn[i]) / (xn[k] - xn[i])
    return iloczyn


def interpolacja_lagranga(x, xn, yn):
    if x in xn:
        for i in range(len(xn)):
            if xn[i] == x:
                return yn[i]

    Pn = 0
    for k in range(len(xn)):
        Pn += yn[k] * Lk(x, k, xn)
    return Pn


'''(Nie działa, musiałam przepisać całość) def macierz_do_newtona(xn, yn):
    tab=[[[0,0,0] for _ in range(len(xn))] for pom in range(len(xn))]
    for i in range(len(xn)):
        tab[i][0][0]=yn[i]
        tab[i][0][1] = xn[i]
        tab[i][0][2] = xn[i]
    for i in range(1,len(xn)):
        for j in range(i,len(xn)):
            tab[j][i][0] = (tab[j][i-1][0]-tab[j-1][i-1][0])/(tab[j][i-1][2]-tab[j-1][i-1][1])
            tab[j][i][1] = tab[j-1][i-1][1]
            tab[j][i][2] = tab[j][i-1][2]
    wspolczynniki=[]
    for i in range(len(xn)):
        wspolczynniki.append(tab[i][i][0])
    return wspolczynniki



def interpolacja_newtona(x, xn, yn):
    wsp = macierz_do_newtona(xn, yn)
    W = wsp[-1]
    for i in range(2,len(xn)+1):
        W*=x
        W+=wsp[-i]
    return W'''


def wspolczynniki_newtona(xn, yn):

    m = len(xn)
    x = copy(xn)
    a = copy(yn)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (xn[k:m] - xn[k - 1])
    return a


def interpolacja_newtona(x, xn, yn):
    tab = wspolczynniki_newtona(xn, yn)
    n = len(xn) - 1
    wynik = tab[n]

    # Schemat Hornera
    for k in range(1, n + 1):
        wynik = tab[n - k] + (x - xn[n - k]) * wynik
    return wynik


def max_blad(x, y):
    blad = 0
    for i in range(len(x)):
        diff = y[i] - funkcja(x[i])
        if blad < abs(diff):
            blad = abs(diff)
    return blad


if __name__ == '__main__':
    wezly = int(input("Podaj liczbe wezlow:\n"))
    rozmieszczenie = input("Podaj sposób rozmieszczenie:(C - czebyszewa, cokolwiek innego - liniowy)\n")

    xn = linspace(0.25, 0.8, wezly)
    if rozmieszczenie == "C":
        for m in range(wezly):
            xn[m] = 0.5 * ((0.8 - 0.25) * cos(pi * (2 * m + 1) / (2 * (wezly - 1) + 2)) + (0.8 + 0.25))

    yn = [funkcja(xn[i]) for i in range(wezly)]
    x = linspace(0.25, 0.8, 100)
    y = [0 for _ in range(100)]
    y_f = [funkcja(x[i]) for i in range(100)]

    # rysowanie wykresu dla interpolacji metodą Lagrange'a
    plt.scatter(xn, yn, color="red")
    for i in range(100):
        y[i] = interpolacja_lagranga(x[i], xn, yn)
    y[0] = 0
    plt.plot(x, y)
    plt.plot(x, y_f, color="pink")
    plt.xlim([0.25, 0.8])
    plt.ylim([-5, 5])
    plt.title("Interpolacja metodą Lagrange'a, węzły: " + str(wezly))
    plt.show()
    print("L:", max_blad(x, y))

    # rysowanie wykresu dla interpolacji metodą Newtona
    for i in range(100):
        y[i] = interpolacja_newtona(x[i], xn, yn)
    plt.plot(x, y)
    plt.xlim([0.25, 0.8])
    plt.ylim([-5, 5])
    plt.plot(x, y_f, color="pink")
    plt.scatter(xn, yn, color="red")
    plt.title("Interpolacja metodą Newtona, węzły: " + str(wezly))
    plt.show()
    print("N:", max_blad(x, y))
