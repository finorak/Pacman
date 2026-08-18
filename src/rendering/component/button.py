from ..core import ImgData


class Button:
    def __init__(self, frames: list[ImgData]) -> None:
        self.frames = frames
        self.current = frames[0]

    def is_hovered(self, mouse_pos: tuple[int, int]) -> bool:
        return (
            self.current.pos_x
            < mouse_pos[0]
            < self.current.pos_x + self.current.width
            and self.current.pos_x
            < mouse_pos[0]
            < self.current.pos_x + self.current.width
        )
