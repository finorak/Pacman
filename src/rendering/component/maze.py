# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    maze.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:25:15 by nyramana         #+#    #+#              #
#    Updated: 2026/08/19 11:16:55 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from mazegenerator import MazeGenerator

from ..core import XMain


class Maze:
    def __init__(
        self, xmain: XMain, size: tuple[int, int], seed: int = 42
    ) -> None:
        self.maze_gen = MazeGenerator(size, seed=seed)
        self.xmain = xmain
