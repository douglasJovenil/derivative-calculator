from typing import List
from errors import UncalculatedPeaksError

class CalculatorValidator(object):
  def __init__(self) -> None: pass

  def validateHasPeaks(self, peaks: List) -> bool:
    if (len(peaks) != 0): return True
    else: raise UncalculatedPeaksError()