# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    game.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: nyramana <nyramana@student.42antananariv  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/19 10:48:47 by nyramana         #+#    #+#              #
#    Updated: 2026/08/20 15:55:40 by nyramana        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #



from ..component import AnimatedSprite, Maze
from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.maze: Maze = Maze(xmain, (16, 16))
        self.maze.generate_maze_image()
        self.atlas = self.load_asset("assets/Pac-man.png")
        self.frames = self.load_game()
        self.move = 0

    def get_input(self, key: int, _) -> str | None:
        if key == 119: # W
            self.move = 1
        elif key == 97: # A
            self.move = 2
        elif key == 115: # S
            self.move = 3
        elif key == 100: # D
            self.move = 4

    def update(self, dt: float) -> None:
        if self.move == 1:
            self.frames["pacman_left"].pos_y -= 2
        elif self.move == 2:
            self.frames["pacman_left"].pos_x -= 2
        elif self.move == 3:
            self.frames["pacman_left"].pos_y += 2
        elif self.move == 4:
            self.frames["pacman_left"].pos_x += 2
        self.frames["pacman_left"].animate(dt)
        self.frames["pacman_right"].animate(dt)
        self.frames["pacman_up"].animate(dt)
        self.frames["pacman_down"].animate(dt)

    def render(self) -> None:
        _ = self.xmain.mlx.mlx_clear_window(
            self.xmain.mlx_ptr, self.xmain.mlx_window
        )
        _ = self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.maze.image.img,
            self.get_center(self.maze.image.width),
            self.get_center(self.maze.image.height, width=False),
        )
        _ = self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            self.frames["pacman_left"].sprite.img,
            int(self.frames["pacman_left"].pos_x),
            int(self.frames["pacman_left"].pos_y)
        )

    def load_game(self) -> dict[str, AnimatedSprite]:
        result: dict[str, AnimatedSprite] = {}
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 0),
            )
            for i in range(3)
        ]
        result["pacman_right"] = AnimatedSprite(pacman, (100, 100))
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 32),
            )
            for i in range(3)
        ]
        result["pacman_left"] = AnimatedSprite(pacman, (200, 100))
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 64),
            )
            for i in range(3)
        ]
        result["pacman_up"] = AnimatedSprite(pacman, (100, 200))
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 96),
            )
            for i in range(3)
        ]
        result["pacman_down"] = AnimatedSprite(pacman, (200, 200))
        return result
