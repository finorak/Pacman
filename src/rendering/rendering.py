from typing import Any

from .screen import MainScreen
from .core import XMain


class Rendering:
    """Class that contains the main rendering part of the program."""

    def __init__(self, win_size: tuple[int, int]) -> None:
        """
        Everything starts here.

        Args:
            win_size (tuple[int, int]): The size of the window.
        """
        self.xmain = XMain(win_size, "Pac-Man")
        self.main_menu = MainScreen(self.xmain)
        self.xmain.mlx.mlx_mouse_hide(self.xmain.mlx_ptr)

    def main_loop(self, _param: Any) -> None:
        """
        Main loop for the rendering.

        Args:
            _param (Any): Parameter needed by the mlx.
        """
        # TODO: Put the logic in here
        self.update()
        self.render()

    def run(self) -> None:
        """Run the program."""
        self.xmain.mlx.mlx_loop_hook(self.xmain.mlx_ptr, self.main_loop, None)
        self.xmain.mlx.mlx_key_hook(self.xmain.mlx_window, self.get_input, None)
        self.xmain.mlx.mlx_hook(self.xmain.mlx_window, 33, 0, self._exit, None)
        self.xmain.mlx.mlx_loop(self.xmain.mlx_ptr)

    def get_input(self, keycode: int, _param: Any) -> None:
        """
        Get the input from the user.

        Args:
            keycode (int): The keycode pressed by the user.
            _param (Any): Parameter needed by the mlx.
        """
        if keycode == 65307 or keycode == 65513:
            self.xmain.mlx.mlx_loop_exit(self.xmain.mlx_ptr)
        self.main_menu.get_input(keycode, _param)

    def render(self) -> None:
        """Render the program in the window."""
        self.main_menu.render()

    def update(self) -> None:
        """Update the logic in the program."""
        self.main_menu.update(0.016)

    def _exit(self, _) -> None:
        self.xmain.mlx.mlx_loop_exit(self.xmain.mlx_ptr)


if __name__ == "__main__":
    rendering = Rendering((800, 600))
    rendering.run()
