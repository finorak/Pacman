# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    core.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 11:06:11 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 15:37:01 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import numpy as np
from mlx import Mlx


class ImgData:
    def __init__(self):
        self.img: int = 0
        self.width: int = 0
        self.height: int = 0
        self.data: np.ndarray | memoryview[int]
        self.sl: int = 0
        self.bpp: int = 0
        self.endian: int = 0


class XMain:
    def __init__(self, win_size: tuple[int, int], title: str):
        self.mlx: Mlx = Mlx()

        self.mlx_ptr: int | None = self.mlx.mlx_init()
        if not self.mlx_ptr:
            raise RuntimeError("Cannot initialize MLX.")

        self.screen_w: int = win_size[0]
        self.screen_h: int = win_size[1]

        self.mlx_window: int | None = self.mlx.mlx_new_window(
            self.mlx_ptr,
            self.screen_w,
            self.screen_h,
            title,
        )
        if not self.mlx_window:
            raise RuntimeError("Cannot initialize the window.")

        self.assets: dict[str, ImgData] = {}
