from .base import Screen
from ..core import XMain


class Game(Screen):
    def __init__(self, xmain: XMain) -> None:
        super().__init__(xmain)

    def get_input(self, key: int, _) -> str | None: ...

    def update(self, dt: float) -> None: ...

    def render(self) -> None: ...
