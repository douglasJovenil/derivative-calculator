from errors import Error

class IsNotXYDatasetError(Error):
  def getMessageError(self) -> str:
    return 'O formato do dataset é inválido! Ele deve ser composto por um conjuto de pontos x;y'