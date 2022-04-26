from abc import abstractmethod


class AbstractAction:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def info(self):
        return self.__class__.__name__
