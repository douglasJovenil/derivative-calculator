from abc import ABC, abstractmethod, ABCMeta

class Error(ABC, Exception):
	def __init__(self):
		super(Error, self).__init__(self.getMessageError())

	@abstractmethod
	def getMessageError(self) -> str: pass

	def __new__(cls, *args, **kwargs):
		abstractmethods = getattr(cls, '__abstractmethods__', None)
		if abstractmethods:
			msg = "Can't instantiate abstract class {name} with abstract method{suffix} {methods}"
			suffix = 's' if len(abstractmethods) > 1 else ''
			raise TypeError(msg.format(name=cls.__name__, suffix=suffix, methods=', '.join(abstractmethods)))
		return super().__new__(cls, *args, **kwargs)