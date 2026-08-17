from typing import Any
from mlx import Mlx


class Rendering:
    """Class that contains the main rendering part of the program."""
    def __init__(self, win_size: tuple[int, int]) -> None:
        """
        Everything starts here.

        Args:
            win_size (tuple[int, int]): The size of the window.
        """
        self._mlx = Mlx()

        self._mlx_ptr = self._mlx.mlx_init()
        self._mlx_window = self._mlx.mlx_new_window(
            self._mlx_ptr, *win_size, "Pac-Man"
        )

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
        self._mlx.mlx_loop_hook(self._mlx_ptr, self.main_loop, None)
        self._mlx.mlx_key_hook(self._mlx_window, self.get_input, None)
        self._mlx.mlx_loop(self._mlx_ptr)

    def get_input(self, keycode: int, _param: Any) -> None:
        """
        Get the input from the user.

        Args:
            keycode (int): The keycode pressed by the user.
            _param (Any): Parameter needed by the mlx.
        """
        # To exit the program with 'q' or 'Alt+F4'
        if keycode == 65307 or keycode == 65513:
            self._mlx.mlx_loop_exit(self._mlx_ptr)

    def render(self) -> None:
        """Render the program in the window."""

    def update(self) -> None:
        """Update the logic in the program."""


if __name__ == "__main__":
    rendering = Rendering((800, 600))
    rendering.run()
