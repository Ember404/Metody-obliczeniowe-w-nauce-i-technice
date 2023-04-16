from matplotlib import pyplot as plt
from matplotlib import axis
from numpy import linspace
from numpy import copy
from math import pi
from math import sin, cos
from numpy import array


def funkcja(x):
    return x * sin((pi * 4) / x)


def pochodna(x):
    return sin((pi * 4) / x) - (4 * pi * cos((pi * 4) / x)) / x


def wspolczynniki_newtona(xn, yn):
    #tworzenie tabeli do przechowywania różnic
    tab = [[0 for _ in range(len(xn) * 2 + 1)] for pom in range(len(xn) * 2)]
    x = copy(xn)
    y = copy(yn)

    #wypełnianie tabeli wartościami x, f(x) i f'(x)
    for i in range(0, len(xn) * 2, 2):
        tab[i][0] = x[int(i / 2)]
        tab[i + 1][0] = x[int(i / 2)]
        tab[i][1] = y[int(i / 2)]
        tab[i + 1][1] = y[int(i / 2)]
        tab[i + 1][2] = pochodna(x[int(i / 2)])

    #obliczanie różnic
    for i in range(2, len(xn) * 2 + 1):
        for j in range(i - 1, len(xn) * 2):
            if i != 2 or j % 2 == 0:
                tab[j][i] = (tab[j][i - 1] - tab[j - 1][i - 1]) / (tab[j][0] - tab[abs(i - 1 - j)][0])

    #pobieranie współczynników wielomianu
    wspolczynniki = []
    for i in range(len(xn) * 2):
        wspolczynniki.append(tab[i][i + 1])

    return wspolczynniki


def interpolacja_newtona(x, xn, yn):
    tab = wspolczynniki_newtona(xn, yn)
    n = len(xn) * 2 - 1
    wynik = tab[n]

    x_pom = [xn[i // 2] for i in range(len(xn) * 2)]

    # Schemat Hornera
    for k in range(1, n + 1):
        wynik = tab[n - k] + (x - x_pom[n - k]) * wynik
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

    #przygotowywanie danych
    xn = linspace(0.25, 0.8, wezly)
    if rozmieszczenie == "C":
        for m in range(wezly):
            xn[m] = 0.5 * ((0.8 - 0.25) * cos(pi * (2 * m + 1) / (2 * (wezly - 1) + 2)) + (0.8 + 0.25))

    yn = [funkcja(xn[i]) for i in range(wezly)]
    x = linspace(0.25, 0.8, 100)
    y = [0 for _ in range(100)]
    y_f = [funkcja(x[i]) for i in range(100)]

    #obliczanie wartości interpolowanego wielomianu
    for i in range(100):
        y[i] = interpolacja_newtona(x[i], xn, yn)

    # rysowanie wykresu dla interpolacji Hermita metodą Newtona
    plt.plot(x, y_f, color="pink")
    plt.plot(x, y)
    plt.xlim([0.25, 0.8])
    plt.ylim([-5, 5])
    plt.scatter(xn, yn, color="red")
    plt.title("Interpolacja metodą Newtona, węzły: " + str(wezly))
    plt.show()
    print("N:", max_blad(x, y))

