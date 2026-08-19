# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    base.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:43 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 13:37:12 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod

from ..core import ImgData, XMain


class ImageError(Exception):
    ...

class Screen(ABC):
    def __init__(self, xmain: XMain) -> None:
        self.xmain: XMain = xmain

        self.assets: dict[str, ImgData] = {}

        self.time = 0.0

    @abstractmethod
    def get_input(self, key: int, _) -> str | None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def render(self) -> None: ...

    def exit(self) -> None:
        for image in self.assets.values():
            self.xmain.mlx.mlx_destroy_image(self.xmain.mlx_ptr, image.img)

    def load_assets(self, files: dict[str, str]) -> dict[str, ImgData]:
        result: dict[str, ImgData] = {}
        for name, path in files.items():
            result[name] = self.load_asset(path)
        return result

    def set_position(self, positions: dict[str, tuple[int, int]]) -> None:
        for name, (x, y) in positions.items():
            self.assets[name].pos_x = x
            self.assets[name].pos_y = y

    def load_asset(self, file: str) -> ImgData:
        image = ImgData()
        tmp = self.xmain.mlx.mlx_png_file_to_image(
            self.xmain.mlx_ptr, file
        )
        if not tmp:
            raise ImageError(f"Cannot load image {image} in path: {file}")
        image.img = tmp[0] if tmp[0] else 0
        image.width, image.height = tmp[1:]
        if not image.img:
            raise ImageError(f"Cannot create image {image} in path: {file}")
        image.data, image.bpp, image.sl, image.iformat = (
            self.xmain.mlx.mlx_get_data_addr(image.img)
        )
        return image

    def get_center(self, lengh: int, width: bool = True) -> int:
        if width:
            return self.xmain.screen_w // 2 - lengh // 2
        return self.xmain.screen_h // 2 - lengh // 2
