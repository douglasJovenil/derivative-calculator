import matplotlib.pyplot as plt
from Calculator import Calculator
from Data import Data
from Point import Point

def main():
    data = Data('../dataset/dataset.csv')
    x, y = data.getDataAsXYArrays()

    points = [Point(x, y) for x, y in zip(x, y)]

    calculator = Calculator(points)
    calculator.derive()
    calculator.calculatePeaks()

    peaksX, peaksY = calculator.getPeaksAsXYArrays()

    plt.grid(color='black', linestyle='-', linewidth=1)
    plt.plot(x, y)
    plt.scatter(peaksX, peaksY, marker='o', color="red")
    plt.show()

if __name__ == "__main__":
    main()