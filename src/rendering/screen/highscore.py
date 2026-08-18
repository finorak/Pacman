from .base import Screen
from ..core import XMain
import math


class HighScore(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.load_assets(
            {
                "logo": "assets/HighScore.png",
                "backtomain": "assets/button/backtomain.png",
            }
        )
        self.set_position(
            {
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

        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["logo"].img,
            int(self.assets["logo"].pos_x),
            int(self.assets["logo"].pos_y),
        )

        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            int(self.assets["backtomain"].img),
            int(self.assets["backtomain"].pos_x),
            int(self.assets["backtomain"].pos_y),
        )

    def update(self, dt: float) -> None:
        self.time += dt
        self.assets["logo"].pos_y = 50 + math.sin(self.time) * 15

    def get_input(self, key: int, _) -> str | None:
        if key == 113:
            return "main"
        print(key)
