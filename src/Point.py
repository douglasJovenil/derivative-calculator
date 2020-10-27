from validators import PointValidator

class Point(object):
  def __init__(self, x: float, y: float):
    self._validator = PointValidator()

    if (self._validator.validateNumberIsIntOrFlot(x)):
      self._x = x
    
    if (self._validator.validateNumberIsIntOrFlot(y)):
      self._y = y

  def getX(self):
    if (self._validator.validateNumberIsNotNull(self._x)):
      return self._x
  
  def getY(self):
    if (self._validator.validateNumberIsNotNull(self._y)):
      return self._y

  def __repr__(self) -> str:
    return f'({self.getX()},{self.getY()})'
  
