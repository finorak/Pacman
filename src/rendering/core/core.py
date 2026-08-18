from mlx import Mlx


class ImgData:
    def __init__(self):
        self.img = None
        self.width = 0
        self.height = 0
        self.data = None
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

        self.window = self.mlx.mlx_new_window(
            self.mlx_ptr,
            self.screen_w,
            self.screen_h,
            title,
        )
        if not self.window:
            raise RuntimeError("Cannot initialize the window.")

        self.assets = {}
