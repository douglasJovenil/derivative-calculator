from numpy import append as np_append
from numpy import arange, array
import matplotlib.pyplot as plt
from sys import float_info
from pandas import read_csv

def main():
    points, peaks = Points(), Points()
    points.x, points.y = getData("./Datasets.csv")
    deriv = array([])
    zero = float_info.min

    erel = lambda x: (x - zero) / zero
    dse = 0.5*10**(-15) 
    step = 2*(points.x[1] - points.x[0])
    tolerance = 0.01

    deriv = ((points.y[i + 1] - points.y[i - 1]) / 2 * step for i in range(1, len(points.y) - 1))
    
    get_point = True
    for i in range(len(points.y[1:-1])):
        curr_deriv = deriv.__next__()
        if (erel(curr_deriv) < dse and get_point and points.y[i] > tolerance):
            peaks.append(points.x[i], points.y[i])
            get_point = False
        elif (curr_deriv > 0): get_point = True

    print(peaks.y)
    plt.grid(color='black', linestyle='-', linewidth=1)
    plt.plot(points.x[:-1], points.y[:-1])
    plt.plot(peaks.x, peaks.y, marker='o')
    plt.show()

def getData(path):
    dataset = read_csv(path, sep=";")
    x = dataset.iloc[:, 0].values.astype("float")
    y = dataset.iloc[:, 1].values.astype("float")
    return (x, y)

class Points(object):
    __slots__ = ("x", "y")

    def __init__(self):
        self.x = array([])
        self.y = array([])

    def append(self, x, y):
        self.x = np_append(self.x, x)
        self.y = np_append(self.y, y)

if __name__ == "__main__":
    main()