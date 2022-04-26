from typing import Any

from core.stm.actions.AbstractAction import AbstractAction


class AvailableAction:

    def __init__(self, action : AbstractAction) -> None:
        self._action = action

    def action(self):
        return self._action

    def __str__(self) -> str:
        return self._action.info()