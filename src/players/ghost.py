from .base import BasePlayer


class Ghost(BasePlayer):
    def __init__(self) -> None:
        super().__init__()

    def move(self, dt: float) -> None:
        ...
