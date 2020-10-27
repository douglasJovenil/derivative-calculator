from errors import Error

class UncalculatedPeaksError(Error):
  def getMessageError(self) -> str:
    return "Os picos ainda não foram calculados ou essa derivada não possui picos!"