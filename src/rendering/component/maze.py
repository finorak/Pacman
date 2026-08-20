# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    maze.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:25:15 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 15:57:12 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from mazegenerator import MazeGenerator

from ..core import Image, XMain


class Maze:
    def __init__(
        self, xmain: XMain, size: tuple[int, int], seed: int = 42
    ) -> None:
        self.maze_gen = MazeGenerator(size, seed=seed)
        self.image_gen = Image(xmain)
        self.size = 38
        self.xmain = xmain
        self.maze = self.maze_gen.maze
        self.image = self.image_gen.generate_image(
            (
                len(self.maze[0]) * self.size + 10,
                len(self.maze) * self.size + 10,
            )
        )

    def generate_maze_image(self) -> None:
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                self.draw_cell((x, y), col)

    def draw_cell(self, pos: tuple[int, int], value: int) -> None:
        real_pos = pos[0] * self.size + 5, pos[1] * self.size + 5
        i = 0
        while (value >> i) != 0:
            if ((value >> i) & 1) != 1:
                i += 1
                continue
            if i == 0:
                self.image_gen.draw_line(
                    self.image,
                    real_pos,
                    (real_pos[0] + self.size, real_pos[1]),
                    5,
                )
            elif i == 1:
                self.image_gen.draw_line(
                    self.image,
                    (real_pos[0] + self.size, real_pos[1]),
                    (real_pos[0] + self.size, real_pos[1] + self.size),
                    5,
                )
            elif i == 2:
                self.image_gen.draw_line(
                    self.image,
                    (real_pos[0], real_pos[1] + self.size),
                    (real_pos[0] + self.size, real_pos[1] + self.size),
                    5,
                )
            else:
                self.image_gen.draw_line(
                    self.image,
                    (real_pos[0], real_pos[1]),
                    (real_pos[0], real_pos[1] + self.size),
                    5,
                )
            i += 1
