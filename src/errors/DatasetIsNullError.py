from errors import Error

class DatasetIsNullError(Error):
  def getMessageError(self) -> str:
    return "O dataset ainda não foi definido!"