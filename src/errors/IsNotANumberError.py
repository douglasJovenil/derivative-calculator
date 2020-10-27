from errors import Error

class IsNotANumberError(Error):
  def getMessageError(self) -> str:
    return "O parâmetro informado não é um número!"