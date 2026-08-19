from src.rendering.rendering import Rendering
from src.parsing.parse import GameModel
import sys


# WITDTH = 800
# HEIGHT = 600
def main() -> None:
    arg = sys.argv[1] if len(sys.argv) > 1 else "config_path.json"
    parse = GameModel(config_path=arg)
    render = Rendering((900, 800))
    render.run()


if __name__ == "__main__":
    main()
