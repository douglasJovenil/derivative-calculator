from numpy import append as np_append
from numpy import arange, array
import matplotlib.pyplot as plt
from noise import pnoise1
from sys import float_info

def main():
    zero = float_info.min
    erel = lambda x: (x - zero) / zero
    dse = 0.5*10**(-15) 
    min_p, max_p, step = -20, 20, 0.001

    x = [x for x in arange(min_p, max_p, step)]
    y = [pnoise1(x) for x in arange(min_p, max_p, step)]
    deriv, peaks_x, peaks_y = list(), list(), list()

    get_point = True
    for i in range(len(y[:-1])):
        deriv.append((y[i + 1] - y[i]) / step)
        if (erel(deriv[i]) < dse and get_point):
            peaks_x.append(x[i])
            peaks_y.append(y[i])
            get_point = False
        elif (deriv[i] > 0): get_point = True

    print(peaks_y)

    plt.grid(color='black', linestyle='-', linewidth=1)
    plt.plot(x[:-1], y[:-1])
    plt.plot(x[:-1], deriv)
    plt.plot(peaks_x, peaks_y, marker='o')
    plt.show()

if __name__ == "__main__":
    main()