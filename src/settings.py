from typing import Any


NORTH = 0b0001
SOUTH = 0b0100
WEST = 0b1000
EAST = 0b0010

# WILL BE USED LATER
# Player
PLAYER_STATE: dict[int, str | int | Any] ={
        119: {
            "x": 0,
            "y": -2,
            "direction": "pacman_up"
        },
        97: {
            "x": -2,
            "y": 0,
            "direction": "pacman_left"
        },
        115: {
            "x": 0,
            "y": 2,
            "direction": "pacman_down"
        },
        100: {
            "x": 2,
            "y": 0,
            "direction": "pacman_right"
            }
        }
