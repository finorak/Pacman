from .sprite import AnimatedSprite


class Ghost:
    def __init__(self, sprites: dict[str, AnimatedSprite]) -> None:
        self.sprites: dict[str, AnimatedSprite] = sprites
        self.current_sprite = self.sprites["pacman_up"]

    def update(self, dt: float) -> None:
        self.current_sprite.animate(dt)

    def move(self, direction: int) -> None:
        ...
