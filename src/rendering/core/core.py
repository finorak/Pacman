from mlx import Mlx


class ImgData:
    def __init__(self):
        self.img = 0
        self.width = 0
        self.height = 0
        self.data: memoryview | None = None
        self.sl = 0
        self.bpp = 0
        self.iformat = 0


class XMain:
    def __init__(self, win_size: tuple[int, int], title: str):
        self.mlx = Mlx()

        self.mlx_ptr = self.mlx.mlx_init()
        if not self.mlx_ptr:
            raise RuntimeError("Cannot initialize MLX.")

        self.screen_w, self.screen_h = win_size

        self.mlx_window = self.mlx.mlx_new_window(
            self.mlx_ptr,
            self.screen_w,
            self.screen_h,
            title,
        )
        if not self.mlx_window:
            raise RuntimeError("Cannot initialize the window.")

        self.assets = {}

    def get_color(self, r: int, g: int, b: int, a: int = 255) -> int:
        return (a << 24) | (b << 16) | (g << 8) | r
