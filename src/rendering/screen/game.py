# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    game.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:47 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 13:24:29 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.maze = self.xmain.generate_image((200, 200))
        self.xmain.draw_line(self.maze, (0, 0), (100, 150))

    def get_input(self, key: int, _) -> str | None: ...

    def update(self, dt: float) -> None: ...

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr, self.xmain.mlx_window
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr, self.xmain.mlx_window, self.maze.img, 100, 100
        )
