from abc import ABC, abstractmethod

from ..core import ImgData, XMain


class Screen(ABC):
    def __init__(self, xmain: XMain) -> None:
        self.xmain: XMain = xmain

        self.assets: dict[str, ImgData] = {}

    @abstractmethod
    def render(self) -> None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def get_input(self, key: int, _) -> str | None: ...

    def load_assets(self, files: dict[str, str]) -> None:
        for name, path in files.items():
            image = ImgData()
            tmp = self.xmain.mlx.mlx_png_file_to_image(self.xmain.mlx_ptr, path)
            if not tmp:
                raise Exception(f"Cannot load image {image} in path: {path}")
            image.img = tmp[0] if tmp[0] else 0
            image.width, image.height = tmp[1:]
            if not image.img:
                raise Exception(f"Cannot create image {image} in path: {path}")
            image.data, image.bpp, image.sl, image.iformat = (
                self.xmain.mlx.mlx_get_data_addr(image.img)
            )
            self.assets[name] = image
