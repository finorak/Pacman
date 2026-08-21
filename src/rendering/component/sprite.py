from ..core import ImgData


class Sprite:
    def __init__(self, sprite: ImgData, pos: tuple[float, float]) -> None:
        self.sprite = sprite
        self.pos_x, self.pos_y = pos


class AnimatedSprite(Sprite):
    def __init__(self, sprites: list[ImgData], pos: tuple[float, float]) -> None:
        self.sprites, self.sprite_index, self.animation_speed = sprites, 0, 15
        super().__init__(sprites[0], pos)

    def animate(self, dt: float) -> None:
        self.sprite_index += self.animation_speed * dt
        self.sprite = self.sprites[int(self.sprite_index) % len(self.sprites)]
