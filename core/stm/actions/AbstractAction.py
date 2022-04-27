from abc import abstractmethod


class AbstractAction:

    def __init__(self) -> None:
        pass

    @abstractmethod
    def info(self):
        return self.__class__.__name__

    @abstractmethod
    def transformation_type(self):
        return "undefined"

    @abstractmethod
    def action_type(self):
        return "undefined"
