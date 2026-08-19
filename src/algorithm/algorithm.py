class Algorithm:
    def __init__(
            self, start_pos: tuple[int, int],
            end_pos: tuple[int, int]
    ) -> None:
        self.start_pos = start_pos
        self.end_pos = end_pos

    def bfs(self) -> list[tuple[int, int]]:
        ...
