# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    instructions.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:54 by nyramana         #+#    #+#              #
#    Updated: 2026/08/21 14:41:00 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import math

from ..core import XMain
from .base import Screen


class InstructionsScreen(Screen):
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
                image.sprite.img,
                int(image.pos_x),
                int(image.pos_y),
            )

    def _render_background(self) -> None:
        image_width = self.assets["back"].sprite.width

        x = self.assets["back"].pos_x

        while x < self.xmain.screen_w:
            _ = self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                self.assets["back"].sprite.img,
                int(x),
                int(self.assets["back"].pos_y),
            )
            x += image_width
