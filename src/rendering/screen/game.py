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



from src.rendering.component import maze
from ...players.ghost import Ghost
from ...players.player import Player
from ..component import AnimatedSprite, Maze
from ..core import XMain
from .base import Screen


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)
        self.maze: Maze = Maze(xmain, (16, 16))
        self.maze.generate_maze_image()
        self.atlas = self.load_asset("assets/Pac-man.png")
        player_frames = self.load_game()
        self.player: Player = Player(player_frames)
        self.ghosts: list[Ghost] = []
        self.player_direction = 97 # A

    def get_input(self, key: int, _) -> str | None:
        if key == 119: # W
            self.player_direction = 119
        elif key == 97: # A
            self.player_direction = 97
        elif key == 115: # S
            self.player_direction = 115
        elif key == 100: # D
            self.player_direction = 100

    def update(self, dt: float) -> None:
        self.player.update(dt, self.maze.maze, self.player_direction)
        for ghost in self.ghosts:
            ghost.update(dt=dt, maze=self.maze.maze)

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
        state = self.player.player_state[self.player_direction]
        player_current_frame = self.player.images[state['direction']]
        _ = self.xmain.mlx.mlx_put_image_to_window(
            self.xmain.mlx_ptr,
            self.xmain.mlx_window,
            player_current_frame.sprite.img,
            int(player_current_frame.pos_x),
            int(player_current_frame.pos_y)
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
        result["pacman_right"] = AnimatedSprite(pacman)
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 32),
            )
            for i in range(3)
        ]
        result["pacman_left"] = AnimatedSprite(pacman)
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 64),
            )
            for i in range(3)
        ]
        result["pacman_up"] = AnimatedSprite(pacman)
        pacman = [
            self.image_loader.copy_sprite(
                self.atlas.sprite,
                self.image_loader.generate_image((32, 32)),
                (32, 32),
                (i * 32, 96),
            )
            for i in range(3)
        ]
        result["pacman_down"] = AnimatedSprite(pacman)
        return result
