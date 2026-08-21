from abc import ABC, abstractmethod

from . import Sprite


class Button(ABC):
    def __init__(self, frames: list[Sprite]) -> None:
        self.frames = frames
        self.current = frames[0]

    def is_hovered(self, mouse_pos: tuple[int, int]) -> bool:
        return (
            self.current.pos_x
            < mouse_pos[0]
            < self.current.pos_x + self.current.sprite.width
            and self.current.pos_x
            < mouse_pos[0]
            < self.current.pos_x + self.current.sprite.width
        )

    @abstractmethod
    def clicked(self) -> str | None:
        # Do some stuff
        # When everything is done
        # return the str (To change the screen/state)
        return
