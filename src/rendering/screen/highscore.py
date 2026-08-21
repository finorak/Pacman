# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    highscore.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:50 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 15:44:28 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


from ..core import XMain
from .base import Screen


class HighScore(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.assets.update(
            self.load_assets(
                {
                    "back": "assets/logo/Back2.png",
                    "logo": "assets/logo/HighScore.png",
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

    def render(self) -> None:
        _ = self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
        )
        self._render_background()
        for name, image in self.assets.items():
            if name == "back":
                continue
            _ = self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                image.sprite.img,
                0,0
            )

    def _render_background(self) -> None:
        image_width = self.assets["back"].sprite.img

        x = 0

        while x < self.xmain.screen_w:
            _ = self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                self.assets["back"].sprite.img,
                int(x),
                0
            )
            x += image_width
