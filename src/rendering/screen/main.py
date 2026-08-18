from .base import Screen
from ..core import XMain


class MainScreen(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.name = "MainScreen"
        self.load_assets(
            {
                "logo": "assets/Logo.png",
                "start": "assets/button/start.png",
                "instructions": "assets/button/instruction.png",
                "highscore": "assets/button/highscore.png",
                "exit": "assets/button/exit.png",
            }
        )

    def get_input(self, key: int, _) -> None | str:
        if key == 65293:
            print("Run the game")
        elif key == 113:
            self.xmain.mlx.mlx_loop_exit(self.xmain.mlx_ptr)
        elif key == 104:
            return "highscore"
        else:
            print(key)

    def update(self, dt: float) -> None: ...

    def render_instruction(self):
        self.xmain.mlx.mlx_clear_window(self.xmain.mlx_ptr, self.xmain.mlx_window)
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["logo"].img,
            800 // 2 - self.assets["logo"].width // 2,
            50,
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["start"].img,
            800 // 2 - self.assets["start"].width // 2,
            250,
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["highscore"].img,
            800 // 2 - self.assets["highscore"].width // 2,
            300,
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["instructions"].img,
            800 // 2 - self.assets["instructions"].width // 2,
            350,
        )
        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["exit"].img,
            800 // 2 - self.assets["exit"].width // 2,
            400,
        )

    def render(self) -> None:
        self.render_instruction()
