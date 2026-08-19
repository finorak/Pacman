from typing import Any

from .base import BasePlayer


class Player(BasePlayer):

    def __init__(
            self, img: Any, x: int = 0,
            y: int = 0, life: int = 3
    ) -> None:
        super().__init__(img, x, y)
        self._life = life

    @property
    def life(self) -> int:
        return self._life

    @life.setter
    def life(self) -> int:
        return self._life
