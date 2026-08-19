from rendering.core import ImgData

class Cell:
    def __init__(
            self, walls: int,
            pos: tuple[int, int],
            max_pos: tuple[int, int],
            color: int
    ) -> None:
        self.pos = pos
        self.max_pos = max_pos
        self.walls = walls
        self.color = color
        self.image = ImgData()

    def draw(self) -> None:
        # Draw a rectangle on the screen
        ...

    def draw_line(self) -> None:
        ...
