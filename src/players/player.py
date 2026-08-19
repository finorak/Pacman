from typing import Any

from .base import BasePlayer


class Player(BasePlayer):
    def __init__(self, img: Any, x: int = 0, y: int = 0) -> None:
        super().__init__(img, x, y)
