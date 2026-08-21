from abc import ABC, abstractmethod
from os.path import samefile
from typing import Any, Optional

from ..rendering.component.sprite import AnimatedSprite


class BasePlayer(ABC):
    """Base Class for player and ghost."""
    def __init__(
            self, images: dict[str, AnimatedSprite],
            x: int = 0, y: int = 0,
            screen_size: tuple[int, int] = (16, 16)) -> None:
        super().__init__()
        self.images = images
        self.screen_size = screen_size
        self._x: int = x
        self._y: int = y

    @abstractmethod
    def move(
            self, dt: float,
            maze: list[list[int]],
            player_current_pos_or_keycode: Optional[tuple[int, int] | int] = None
    ) -> None: ...

    @abstractmethod
    def update(self, dt: float, maze: list[list[int]], player_direction: Any | int = None) -> None: ...

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value

    def can_go(
            self,
            state: dict[str, Any],
            maze: list[list[int]]
    ) -> bool:
        rows: int = len(maze)
        cols: int = len(maze[0])
        dx, dy = state['x'], state['y']
        new_x, new_y = self.x + dx, self.y + dy
        if rows <= new_x < 0 > new_y >= cols:
            return False
        return False
