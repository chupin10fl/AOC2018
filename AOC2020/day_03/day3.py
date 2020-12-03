from __future__ import annotations
from enum import IntEnum, unique

import numpy as np

from AOC2020.helpers import GIT_DIR


def open_input() -> list[int]:
    with open(f'{GIT_DIR}/day_03/input.txt', 'r') as fh:
        return fh.read().strip()


TEST_CASE = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


@unique
class GeographyType(IntEnum):
    EMPTY = 1
    TREE = 2

    @staticmethod
    def from_str(s: str) -> GeographyType:
        mappings = {
            '.': GeographyType.EMPTY,
            '#': GeographyType.TREE,
        }
        return mappings[s]


class Toboggan:
    def __init__(self):
        self.pos = np.array([0, 0])
        self.trees_hit = []

    def on_tree(self, grid: np.ndarray) -> bool:
        if grid[self.pos[0], self.pos[1]] == GeographyType.TREE:
            self.trees_hit.append(self.pos)
            return True
        else:
            return False

    @property
    def num_trees_hit(self) -> int:
        return len(self.trees_hit)


def string_to_np(trees: str) -> np.ndarray:
    treegrid = np.array(
        [[GeographyType.from_str(char) for char in line] for line in trees.split('\n')],
        dtype=GeographyType
    )
    return treegrid


def step(tob: Toboggan, treegrid: np.ndarray) -> bool:
    STEPSIZE = np.array([1, 3])
    grid_height, grid_width = treegrid.shape
    newpos = tob.pos + STEPSIZE
    if newpos[0] >= grid_height:
        return False
    if newpos[1] >= grid_width:
        newpos[1] -= grid_width
    tob.pos = newpos
    tob.on_tree(treegrid)
    return True


if __name__ == '__main__':
    grid = string_to_np(open_input())
    mytob = Toboggan()
    while step(mytob, grid):
        print(mytob.pos)
    print(mytob.num_trees_hit)