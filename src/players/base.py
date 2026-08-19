from abc import ABC, abstractmethod


class BasePlayer(ABC):
    """Base Class for player and ghost."""
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def move(self, dt: float) -> None: ...
