from .base import Screen
from ..core import XMain
import math


class MainScreen(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.load_assets(
            {
                "logo": "assets/Logo.png",
                "start": "assets/button/start.png",
                "instructions": "assets/button/instruction.png",
                "highscore": "assets/button/highscore.png",
                "exit": "assets/button/exit.png",
            }
        )
        self.set_position(
            {
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
            print("See the instruction")
        else:
            print(key)

    def update(self, dt: float) -> None:
        self.time += dt
        self.assets["logo"].pos_y = 50 + math.sin(self.time * 2) * 15
        self.assets["logo"].pos_x = (
            self.get_center(self.assets["logo"].width)
            - 10
            - math.sin(60 + self.time * 2) * 20
        )

    def render_instruction(self):
        self.xmain.mlx.mlx_clear_window(self.xmain.mlx_ptr, self.xmain.mlx_window)
        for _, image in self.assets.items():
            self.xmain.mlx.mlx_put_image_to_window(
                self.xmain.mlx_ptr,
                self.xmain.mlx_window,
                image.img,
                int(image.pos_x),
                int(image.pos_y),
            )

    def render(self) -> None:
        self.render_instruction()
