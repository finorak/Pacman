from typing import Any, Optional

from .base import BasePlayer


class Player(BasePlayer):

    def __init__(
            self, img: Any, x: int = 0,
            y: int = 0, life: int = 3
    ) -> None:
        super().__init__(img, x, y)
        self._life = life

    def move(
            self, dt: float, maze: list[list[int]],
            player_current_pos_or_keycode: Optional[tuple[int, int] | int] = None
    ) -> None:
        if isinstance(player_current_pos_or_keycode, tuple):
            return
        # this tell us that `player_current_pos_or_keycode` is keycode

    @property
    def life(self) -> int:
        return self._life

    @life.setter
    def life(self) -> int:
        return self._life
