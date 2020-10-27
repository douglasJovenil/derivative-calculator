from pandas.core.frame import DataFrame
from errors import IsNotXYDatasetError, DatasetIsNullError

class DataValidator(object):
  def __init__(self): pass

  def validateIsXYDataset(self, data: DataFrame) -> bool:
    if (len(data.columns) == 2):
      return True
    else: raise IsNotXYDatasetError()
  
  def validateDatasetIsNotNull(self, data: DataFrame) -> bool:
    if (isinstance(data, DataFrame)):
      return True
    else: raise DatasetIsNullError()