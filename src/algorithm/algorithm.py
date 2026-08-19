from ..rendering.component.maze import Maze
from ..settings import NORTH, SOUTH, EAST, WEST
from collections import deque


class Algorithm:
    def __init__(
            self, start_pos: tuple[int, int],
            end_pos: tuple[int, int]
    ) -> None:
        self.start_pos = start_pos
        self.end_pos = end_pos

    def bfs(self, maze_gen: Maze) -> list[tuple[int, int]]:
        # This variable isn't in it yet
        # wating for it to be finished.
        maze: list[list[int]] = maze_gen.maze  # type: ignore[attr-defined]
        stack: deque = deque([self.start_pos])
        came_from: dict[tuple[int, int], tuple[int, int]] = {}
        seen: set[tuple[int, int]] = set()
        while stack:
            current = stack.popleft()
            if current == self.end_pos:
                return self._reconstruct_path(came_from)
            seen.add(current)
            neighboors = self._find_neighboor(current, maze, seen)
            for cell in neighboors:
                came_from[cell] = current
            stack.extend(neighboors)
        return []

    def _reconstruct_path(
            self,
            came_from: dict[tuple[int, int], tuple[int, int]]
    ) -> list[tuple[int, int]]:
        paths: list[tuple[int, int]] = []
        current = came_from[self.end_pos]
        while True:
            if current == self.start_pos:
                break
            paths.append(current)
            current = came_from[current]
        return paths

    def _find_neighboor(
            self, current: tuple[int, int],
            maze: list[list[int]], seen: set[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        rows: int = len(maze)
        cols: int = len(maze[0])
        x, y = current
        neighboors: list[tuple[int, int]] = []
        if x - 1 >= 0 and (x - 1, y) not in seen and maze[x - 1][y] & NORTH:
            neighboors.append((x - 1, y))
        if x + 1 < rows and (x + 1, y) not in seen and maze[x + 1][y] & SOUTH:
            neighboors.append((x + 1, y))
        if y - 1 >= 0 and (x, y - 1) not in seen and maze[x][y - 1] & EAST:
            neighboors.append((x, y - 1))
        if y + 1 < cols and (x, y + 1) not in seen and maze[x][y + 1] & WEST:
            neighboors.append((x, y + 1))
        return neighboors
