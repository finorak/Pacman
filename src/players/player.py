from typing import Any

from .base import BasePlayer


class Player(BasePlayer):

    def __init__(
            self, frames: Any, x: int = 0,
            y: int = 0, life: int = 3,
    ) -> None:
        super().__init__(frames, x, y)
        self._life = life
        self.player_state: dict[int, dict[str, Any]] = {
                119: {
                    "dx_pos": 0,
                    "dy_pos": -2,
                    "x": 0,
                    "y": -1,
                    "direction": "pacman_up"
                    },
                97: {
                    "dx_pos": -2,
                    "dy_pos": 0,
                    "x": -1,
                    "y": 0,
                    "direction": "pacman_left"
                    },
                115: {
                    "dx_pos": 0,
                    "dy_pos": 2,
                    "x": 0,
                    "y": 1,
                    "direction": "pacman_down"
                    },
                100: {
                    "dx_pos": 2,
                    "dy_pos": 0,
                    "x": 1,
                    "y": 0,
                    "direction": "pacman_right"
                    }
                }

    def move(
            self, dt: float, maze: list[list[int]],
            player_current_pos_or_keycode: Any | None = None
    ) -> None:
        if isinstance(player_current_pos_or_keycode, tuple):
            return
        # this tell us that `player_current_pos_or_keycode` is keycode

    def update(self, dt: float, maze: list[list[int]], player_direction: Any = None) -> None:
        if player_direction is None:
            return
        state = self.player_state[player_direction]
        if not self.can_go(state, maze):
            return
        player_current_frame = self.images[state['direction']]
        dx_pos = state['dx_pos']
        dy_pos = state['dy_pos']
        player_current_frame.pos_x += dx_pos
        player_current_frame.pos_y += dy_pos
        # update player position
        self.x = player_current_frame.pos_x // 16
        self.y = player_current_frame.pos_y // 16
        self.update_other_sprites_pos(player_direction)
        player_current_frame.animate(dt)

    @property
    def life(self) -> int:
        return self._life

    @life.setter
    def life(self) -> int:
        return self._life

    def update_other_sprites_pos(self, player_direction: int) -> None:
        # This function is way to arcaic
        # will be updated inside AnimatedSprite or
        # will use this one instead
        current_state = self.player_state[player_direction]
        pos_x = self.images[current_state['direction']].pos_x
        pos_y = self.images[current_state['direction']].pos_y
        for state in self.player_state:
            if state == player_direction:
                continue
            other_state = self.player_state[state]
            self.images[other_state['direction']].pos_x = pos_x
            self.images[other_state['direction']].pos_y = pos_y
