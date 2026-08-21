from abc import ABC, abstractmethod
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
    def update(
            self, dt: float,
            maze: list[list[int]],
            player_direction: Any | int = None
    ) -> None: ...

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
            self, maze: list[list[int]],
            new_pos: tuple[int, int],
            old_pos: tuple[int, int]
    ) -> bool:
        # verifying if the cell we want to go
        # is a neighboor of the current cell.
        new_x, new_y = new_pos
        old_x, old_y = old_pos
        old_cell = maze[old_x][old_y]
        new_cell = maze[new_x][new_y]
        return not old_cell & new_cell

    def cell_is_valid(
            self,
            state: dict[str, Any],
            maze: list[list[int]]
    ) -> bool:
        rows: int = len(maze)
        cols: int = len(maze[0])
        dx, dy = state['x'], state['y']
        return True
        if rows <= self.x + dx > 0 or cols <= self.y > 0:
            return False
        if not self.can_go(maze, (self.x + dx, self.y + dy), (self.x, self.y)):
            return False
        return True
