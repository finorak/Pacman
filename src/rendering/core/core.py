# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    core.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 11:06:11 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 16:21:41 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import numpy as np
from mlx import Mlx


class ImgData:
    def __init__(self):
        self.img = 0
        self.width = 0
        self.height = 0
        self.data: np.ndarray
        self.sl = 0
        self.bpp = 0
        self.iformat = 0
        self.pos_x: float = 0
        self.pos_y: float = 0


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
        return (a << 24) | (r << 16) | (g << 8) | b

    def generate_image(self, size: tuple[int, int]) -> ImgData:
        img_data = ImgData()
        tmp = self.mlx.mlx_new_image(self.mlx_ptr, size[0], size[1])
        if not tmp:
            raise RuntimeError("Cannot initialize cell Image")
        img_data.width, img_data.height = size
        img_data.img = tmp
        img_data.data, img_data.bpp, img_data.sl, img_data.iformat = (
            self.mlx.mlx_get_data_addr(tmp)
        )
        img_data.pos_x, img_data.pos_y = 100, 100
        img_data.data[:] = b"\x00" * len(img_data.data)
        return img_data

    def put_pixel(
        self,
        img: ImgData,
        pos: tuple[int, int],
        color: int,
    ) -> None:
        if 0 <= pos[0] < img.width and 0 <= pos[1] < img.height:
            offset = pos[1] * img.sl + pos[0] * (img.bpp // 8)
            img.data[offset : offset + 4] = color.to_bytes(4, "little")

    def draw_line(
        self,
        img: ImgData,
        start: tuple[int, int],
        end: tuple[int, int],
        thickness: int = 1,
        color: int = 0xFFFFFFFF,
    ) -> None:
        # Bresenham's line algorithm + Thickness

        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])
        sx = 1 if start[0] < end[0] else -1
        sy = 1 if start[1] < end[1] else -1
        err = dx - dy

        x, y = start[0], start[1]

        while True:
            for dx_thick in range(-thickness // 2, thickness // 2 + 1):
                for dy_thick in range(-thickness // 2, thickness // 2 + 1):
                    self.put_pixel(img, (x + dx_thick, y + dy_thick), color)

            if x == end[0] and y == end[1]:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
