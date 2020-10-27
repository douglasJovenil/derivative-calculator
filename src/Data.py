from pandas import read_csv
from validators import DataValidator

class Data(object):
  def __init__(self, path: str):
    self.path = path
    self._validator = DataValidator()
    self._data = self._readCsv()
  
  def getDataAsXYArrays(self):
    if (self._validator.validateDatasetIsNotNull(self._data)):
      x = self._data.iloc[:, 0].values.astype("float")
      y = self._data.iloc[:, 1].values.astype("float")
      return x, y
  
  def _readCsv(self):
    data = read_csv(self.path, sep=';')
    if (self._validator.validateIsXYDataset(data)):
      return data
  
  def show(self):
    if (self._validator.validateDatasetIsNotNull(self._data)):
      print(self._data)
  