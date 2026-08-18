from abc import ABC, abstractmethod
from ..core import XMain


class Screen(ABC):
    def __init__(self, xmain: XMain) -> None:
        self.name = ""

        self.xmain = xmain

        self.assets = {}

    @abstractmethod
    def render(self) -> None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def get_input(self) -> None: ...
