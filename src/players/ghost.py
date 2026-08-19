# package used to move ghost in random
# direction if the player isn't in its radius range
import random
from typing import Any, Optional

from .base import BasePlayer


class Ghost(BasePlayer):
    def __init__(self, img: Any, x: int = 0, y: int = 0) -> None:
        super().__init__(img, x, y)
        self.radius: int = 20
        self.find_player: bool = False

    def move(self, dt: float, player_current_pos: Optional[tuple[int, int]] = None) -> None:
        # using this, we'll move the ghost in a maner
        # that is random.
        # moving in random direction
        if player_current_pos is not None and self._player_is_in_range(player_current_pos):
            self._find_path(player_current_pos)
            return
        direction_value: int = random.randint(0, 4) % 4
        if direction_value == 0:  # LEFT
            self.x -= 1
        elif direction_value == 1:  # UP
            self.y -= 1
        elif direction_value == 2:  # RIGHT
            self.x += 1
        else:  # DOWN
            self.y += 1

    def _player_is_in_range(self, player_pos: tuple[int, int]) -> bool:
        # verify if player is in the visual of the ghost
        if player_pos is None:
            return False
        x = player_pos[0]
        y = player_pos[1]
        return ((x - self.x) ** 0.2) + ((y - self.y) ** 0.2) < (self.radius ** 0.2)

    def _find_path(self, player_current_pos: tuple[int, int]) -> bool:
        ...
