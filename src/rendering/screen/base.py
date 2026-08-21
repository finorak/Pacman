# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    base.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:43 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 15:46:36 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from os import walk
from os.path import join

import numpy as np

from ..component import Sprite
from ..core import Image, ImgData, XMain


class ImageError(Exception): ...


class Screen(ABC):
    def __init__(self, xmain: XMain) -> None:
        self.xmain: XMain = xmain

        self.assets: dict[str, Sprite] = {}

        self.time: float = 0.0

        self.image_loader = Image(xmain)



    @abstractmethod
    def get_input(self, key: int, _: object) -> str | None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def render(self) -> None: ...

    def exit(self) -> None:
        for image in self.assets.values():
            _ = self.xmain.mlx.mlx_destroy_image(self.xmain.mlx_ptr, image.sprite.img)

    def load_assets(self, files: dict[str, str]) -> dict[str, Sprite]:
        result: dict[str, Sprite] = {}
        for name, path in files.items():
            result[name] = self.load_asset(path)
        return result

    def load_asset(self, file: str) -> Sprite:
        image = ImgData()
        tmp = self.xmain.mlx.mlx_png_file_to_image(self.xmain.mlx_ptr, file)
        if not tmp:
            raise ImageError(f"Cannot load image {image} in path: {file}")
        image.img = tmp[0] if tmp[0] else 0
        image.width, image.height = tmp[1:]
        if not image.img:
            raise ImageError(f"Cannot create image {image} in path: {file}")
        image.data, image.bpp, image.sl, image.endian = (
            self.xmain.mlx.mlx_get_data_addr(image.img)
        )

        image.data = np.array(image.data)
        return Sprite(image, (0,0))

    def load_from_folder(self, *path: str) -> list[Sprite]:
        result: list[Sprite] = []
        for folder_path, _, file_names in walk(join(*path)):
            for file_name in file_names:
                result.append(self.load_asset(join(folder_path, file_name)))
        return result

    def get_center(self, lengh: int, width: bool = True) -> int:
        if width:
            return self.xmain.screen_w // 2 - lengh // 2
        return self.xmain.screen_h // 2 - lengh // 2

    def set_position(self, src: dict[str, Sprite], position: dict[str, tuple[int, int]]) -> None:
        for name, value in position.items():
            src[name].pos_x, src[name].pos_y = value
