from collections import deque

from ..settings import EAST, NORTH, SOUTH, WEST


class Algorithm:
    def __init__(
            self, start_pos: tuple[int, int],
            end_pos: tuple[int, int]
    ) -> None:
        self.start_pos = start_pos
        self.end_pos = end_pos

    def bfs(self, maze: list[list[int]]) -> list[tuple[int, int]]:
        # This variable isn't in it yet
        # wating for it to be finished.
        stack: deque = deque([self.start_pos])
        came_from: dict[tuple[int, int], tuple[int, int]] = {}
        seen: set[tuple[int, int]] = set()
        while stack:
            current = stack.popleft()
            if current in seen:
                continue
            if current == self.end_pos:
                return self._reconstruct_path(came_from)
            seen.add(current)
            neighboors = self._find_neighboor(current, maze)
            filtered_neighboors = []
            for cell in neighboors:
                if cell in seen:
                    continue
                filtered_neighboors.append(cell)
                came_from[cell] = current
            stack.extend(filtered_neighboors)
        return []

    def _reconstruct_path(
            self,
            came_from: dict[tuple[int, int], tuple[int, int]]
    ) -> list[tuple[int, int]]:
        paths: list[tuple[int, int]] = []
        current = came_from[self.end_pos]
        while current is not None:
            if current == self.start_pos:
                break
            paths.append(current)
            current = came_from[current]
        return paths

    def _find_neighboor(
            self, current: tuple[int, int],
            maze: list[list[int]]
    ) -> list[tuple[int, int]]:
        rows: int = len(maze)
        cols: int = len(maze[0])
        x, y = current
        neighboors: list[tuple[int, int]] = []
        if x - 1 >= 0 and maze[x - 1][y] & NORTH == 0:
            neighboors.append((x - 1, y))
        if x + 1 < rows and maze[x + 1][y] & SOUTH == 0:
            neighboors.append((x + 1, y))
        if y - 1 >= 0 and maze[x][y - 1] & EAST == 0:
            neighboors.append((x, y - 1))
        if y + 1 < cols and maze[x][y + 1] & WEST == 0:
            neighboors.append((x, y + 1))
        return neighboors
