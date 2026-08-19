# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    rendering.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:49:09 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 13:25:06 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import time
from typing import Any

from .core import XMain
from .screen import Game, HighScore, Instructions, Main, Screen


class Rendering:
    """Class that contains the main rendering part of the program."""

    def __init__(self, win_size: tuple[int, int]) -> None:
        """
        Everything starts here.

        Args:
            win_size (tuple[int, int]): The size of the window.
        """
        self.xmain = XMain(win_size, "Pac-Man")
        self.states: dict[str, Screen] = {
            "main": Main(self.xmain),
            "highscore": HighScore(self.xmain),
            "instructions": Instructions(self.xmain),
            "game": Game(self.xmain)
        }
        self.current_screen = self.states["main"]

        self.previous_time = time.perf_counter()

    def main_loop(self, _param: Any) -> None:
        """
        Main loop for the rendering.

        Args:
            _param (Any): Parameter needed by the mlx.
        """
        # TODO: Put the logic in here
        current_time = time.perf_counter()
        dt = current_time - self.previous_time
        self.previous_time = current_time
        self.update(dt)
        self.render()

    def run(self) -> None:
        """Run the program."""
        _ = self.xmain.mlx.mlx_loop_hook(
            self.xmain.mlx_ptr, self.main_loop, None
        )
        _ = self.xmain.mlx.mlx_key_hook(
            self.xmain.mlx_window, self.get_input, None
        )
        _ = self.xmain.mlx.mlx_hook(
            self.xmain.mlx_window, 33, 0, self._exit, None
        )
        _ = self.xmain.mlx.mlx_loop(self.xmain.mlx_ptr)

    def get_input(self, keycode: int, _param: Any) -> None:
        """
        Get the input from the user.

        Args:
            keycode (int): The keycode pressed by the user.
            _param (Any): Parameter needed by the mlx.
        """
        current = self.current_screen.get_input(keycode, _param)
        if current:
            self.current_screen = self.states[current]

    def render(self) -> None:
        """Render the program in the window."""
        self.current_screen.render()

    def update(self, dt: float) -> None:
        """Update the logic in the program."""
        self.current_screen.update(dt)

    def _exit(self, _) -> None:
        for screen in self.states.values():
            screen.exit()
        self.xmain.mlx.mlx_release(self.xmain.mlx_ptr)
        self.xmain.mlx.mlx_loop_exit(self.xmain.mlx_ptr)


if __name__ == "__main__":
    rendering = Rendering((900, 800))
    rendering.run()
