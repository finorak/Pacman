from abc import ABC, abstractmethod
from typing import Any, Optional

from ..rendering.core.core import ImgData


class BasePlayer(ABC):
    """Base Class for player and ghost."""
    def __init__(self, img: Any, x: int = 0, y: int = 0) -> None:
        super().__init__()
        self.image = ImgData()
        self.image.img = img
        self._x: int = x
        self._y: int = y

    @abstractmethod
    def move(
            self, dt: float,
            maze: list[list[int]],
            player_current_pos_or_keycode: Optional[tuple[int, int] | int] = None
    ) -> None: ...

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self) -> int:
        return self._y
