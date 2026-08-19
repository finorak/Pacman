# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    game.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:47 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 16:59:40 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..component import Maze
from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.maze = Maze(xmain, (16, 16))
        self.maze.generate_maze_image()
        self.frames = self.load_from_folder("assets/other")

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
            self.get_center(self.maze.image.width),
            self.get_center(self.maze.image.height, width=False),
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.frames[1].img,
            self.get_center(self.frames[1].width),
            self.get_center(self.frames[1].height, width=False),
        )
