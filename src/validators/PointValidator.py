from errors import IsNotANumberError, PointIsNullError

class PointValidator(object):
  def __init__(self): pass

  def validateNumberIsIntOrFlot(self, number) -> bool:
    if (isinstance(number, int) or isinstance(number, float)):
      return True
    else: raise IsNotANumberError()
  
  def validateNumberIsNotNull(self, number) -> bool:
    if (number != None):
      return True
    else: raise PointIsNullError()