# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    game.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:47 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 14:37:12 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..component import Maze
from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.maze = Maze(xmain, (30, 30))
        self.maze.generate_maze_image()

    def get_input(self, key: int, _) -> str | None: ...

    def update(self, dt: float) -> None: ...

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr, self.xmain.mlx_window
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.maze.image.img,
            0,
            0,
        )
