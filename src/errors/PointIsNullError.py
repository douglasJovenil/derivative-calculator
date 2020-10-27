from errors import Error

class PointIsNullError(Error):
  def getMessageError(self) -> str:
    return "O ponto ainda não foi definido!"