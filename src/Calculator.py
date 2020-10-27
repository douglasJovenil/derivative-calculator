from sys import float_info
from typing import List, Tuple
from Point import Point
from validators import CalculatorValidator

class Calculator(object):
  def __init__(self, points: List[Point]): 
    self._validator = CalculatorValidator()
    self._derivatives: Tuple[float] = []
    self._peaks: List[Point] = []
    self._points = points
    # Valor proximo do minimo, se for o minimo vai ocorrer overflow
    self._zero = float_info.min * 10**100
    self._dse = 0.5*10**(-15) 
    self._tolerance = 0.01

  def derive(self):
    # Derivada usando a definicao considerando um step = 1
    self._derivatives = ((self._points[i+1].getY() - self._points[i].getY()) for i in range(1, len(self._points) - 1))
  
  def calculatePeaks(self):
    get_point = True
    for i in range(len(self._points[1:-1])):
        curr_deriv = self._derivatives.__next__()
        if (self._erel(curr_deriv) < self._dse and self._points[i].getY() > self._tolerance and get_point):
            self._peaks.append(self._points[i])
            get_point = False
        elif (curr_deriv > 0): get_point = True
    
  def _erel(self, x):
    return (x - self._zero) / self._zero

  def getPeaksAsXYArrays(self):
    if (self._validator.validateHasPeaks(self._peaks)):
      x = [point.getX() for point in self._peaks]
      y = [point.getY() for point in self._peaks]
      return x, y
