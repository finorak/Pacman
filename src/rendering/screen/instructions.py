# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    instructions.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:54 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 09:10:01 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import math
import random

from ..core import XMain
from .base import Screen


class Instructions(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.assets.update(
            self.load_assets(
                {
                    "back": "assets/logo/Back2.png",
                    "logo": "assets/logo/Instructions.png",
                    "backtomain": "assets/button/backtomain.png",
                }
            )
        )
        self.set_position(
            {
                "back": (0, random.randint(-400, 0)),
                "logo": (
                    self.get_center(self.assets["logo"].width),
                    50,
                ),
                "backtomain": (
                    self.get_center(self.assets["backtomain"].width),
                    550,
                ),
            }
        )

    def get_input(self, key: int, _) -> str | None:
        if key == 113:
            return "main"
        print(key)

    def update(self, dt: float) -> None:
        self.time += dt
        self.assets["logo"].pos_y = 50 + math.sin(self.time) * 15
        self.assets["back"].pos_x -= dt * 30

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
        )
        self._render_background()
        for name, image in self.assets.items():
            if name == "back":
                continue
            self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                image.img,
                int(image.pos_x),
                int(image.pos_y),
            )

    def _render_background(self) -> None:
        image_width = self.assets["back"].width

        x = self.assets["back"].pos_x

        while x < self.xmain.screen_w:
            _ = self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                self.assets["back"].img,
                int(x),
                int(self.assets["back"].pos_y),
            )
            x += image_width
