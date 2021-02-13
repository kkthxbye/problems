from typing import List, Tuple
from itertools import product
from collections import deque


def eligible_neighbours(grid: List[List[int]], coords: Tuple[int, int]) -> List[Tuple[int, int]]:
    if grid[coords[0]][coords[1]] == 1:
        return []
    n = len(grid)
    offsets = [-1, 0, 1]
    return list(filter(
        lambda x: x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < n and grid[x[0]][x[1]] != 1,
        ((coords[0] + offset[0], coords[1] + offset[1])
         for offset in filter(
             lambda x: not (x[0] == 0 and x[1] == 0),
             product(offsets, offsets),
        )),
    ))


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    start = (0, 0)
    n = len(grid) - 1
    if start == (n, n):
        return 1
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbour in eligible_neighbours(grid, node):
            current_path = path + [neighbour]
            if neighbour == (n, n):
                return len(current_path)
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, current_path))
    return -1


print(shortestPathBinaryMatrix([[0, 1], [1, 0]]))

print(shortestPathBinaryMatrix([
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]))


print(shortestPathBinaryMatrix([
    [0, 0, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]))

print(shortestPathBinaryMatrix([
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]))

print(shortestPathBinaryMatrix([
    [0],
]))
