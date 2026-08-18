from .base import Screen
from ..core import XMain


class HighScore(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.load_assets({"logo": "assets/HighScore.png"})

    def render(self) -> None:
        self.xmain.mlx.mlx_clear_window(self.xmain.mlx_ptr, self.xmain.mlx_window)

        self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.assets["logo"].img,
            800 // 2 - self.assets["logo"].width // 2,
            50,
        )

    def update(self, dt: float) -> None: ...

    def get_input(self, key: int, _) -> str | None:
        if key == 65307:
            return "main"
        print(key)
