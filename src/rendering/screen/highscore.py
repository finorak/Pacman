from .base import Screen
from ..core import XMain
import math
import random


class HighScore(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.load_assets(
            {
                "back2": "assets/Back2.png",
                "logo": "assets/HighScore.png",
                "backtomain": "assets/button/backtomain.png",
            }
        )
        self.set_position(
            {
                "back2": (0, random.randint(-300, 0)),
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

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(self.xmain.mlx_ptr, self.xmain.mlx_window)

        for _, image in self.assets.items():
            self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                image.img,
                int(image.pos_x),
                int(image.pos_y),
            )

    def update(self, dt: float) -> None:
        self.time += dt
        self.assets["logo"].pos_y = 50 + math.sin(self.time) * 15
        self.assets["back2"].pos_x -= dt * 30

    def get_input(self, key: int, _) -> str | None:
        if key == 113:
            return "main"
        print(key)
