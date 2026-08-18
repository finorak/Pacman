from .base import Screen
from ..core import XMain
import math
import random


class Main(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.load_assets(
            {
                "back": "assets/Back.png",
                "logo": "assets/Logo.png",
                "start": "assets/button/start.png",
                "instructions": "assets/button/instruction.png",
                "highscore": "assets/button/highscore.png",
                "exit": "assets/button/exit.png",
            }
        )
        self.set_position(
            {
                "back": (0, random.randint(-400, 0)),
                "logo": (
                    self.get_center(self.assets["logo"].width),
                    50,
                ),
                "start": (
                    self.get_center(self.assets["start"].width),
                    250,
                ),
                "instructions": (
                    self.get_center(self.assets["instructions"].width),
                    300,
                ),
                "highscore": (
                    self.get_center(self.assets["highscore"].width),
                    350,
                ),
                "exit": (
                    self.get_center(self.assets["exit"].width),
                    400,
                ),
            }
        )

    def get_input(self, key: int, _) -> None | str:
        if key == 65293:
            print("Run the game")
        elif key == 113:
            self.xmain.mlx.mlx_loop_exit(self.xmain.mlx_ptr)
        elif key == 104:
            return "highscore"
        elif key == 105:
            return "instructions"
        else:
            print(key)

    def update(self, dt: float) -> None:
        self.time += dt
        self.assets["logo"].pos_y = 50 + math.sin(self.time * 2) * 10
        self.assets["logo"].pos_x = (
            self.get_center(self.assets["logo"].width)
            - 10
            + math.cos(10 + self.time * 2) * 10
        )
        self.assets["back"].pos_x -= dt * 30

    def render_instruction(self):
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

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
        )
        self.render_background()
        self.render_instruction()

    def render_background(self) -> None:
        image_width = self.assets["back"].width

        x = self.assets["back"].pos_x

        while x < self.xmain.screen_w:
            self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                self.assets["back"].img,
                int(x),
                int(self.assets["back"].pos_y),
            )
            x += image_width
