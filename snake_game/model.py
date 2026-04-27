from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple

Cell = Tuple[int, int]

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def vector(self) -> Cell:
        return self.value

    def opposite(self, other: "Direction") -> bool:
        return (self.vector[0] + other.vector[0] == 0 and
                self.vector[1] + other.vector[1] == 0)


class FoodFactory:
    @staticmethod
    def create_food(width: int, height: int, exclude: List[Cell]) -> Cell:
        candidates = [
            (x, y)
            for x in range(width)
            for y in range(height)
            if (x, y) not in exclude
        ]
        return random.choice(candidates)


@dataclass
class GameState:
    width: int
    height: int
    snake: List[Cell]
    direction: Direction
    food: Cell
    score: int = 0
    game_over: bool = False


class GameModel:
    def __init__(self, width: int = 20, height: int = 15) -> None:
        self.state = GameState(
            width=width,
            height=height,
            snake=[(width // 2, height // 2)],
            direction=Direction.RIGHT,
            food=FoodFactory.create_food(width, height, [(width // 2, height // 2)]),
        )

    def change_direction(self, new_direction: Direction) -> None:
        if not new_direction.opposite(self.state.direction):
            self.state.direction = new_direction

    def step(self) -> None:
        if self.state.game_over:
            return

        head_x, head_y = self.state.snake[0]
        move_x, move_y = self.state.direction.vector
        new_head = (head_x + move_x, head_y + move_y)

        if self._detect_collision(new_head):
            self.state.game_over = True
            return

        self.state.snake.insert(0, new_head)

        if new_head == self.state.food:
            self.state.score += 1
            self.state.food = FoodFactory.create_food(
                self.state.width,
                self.state.height,
                self.state.snake,
            )
        else:
            self.state.snake.pop()

    def reset(self) -> None:
        self.state = GameState(
            width=self.state.width,
            height=self.state.height,
            snake=[(self.state.width // 2, self.state.height // 2)],
            direction=Direction.RIGHT,
            food=FoodFactory.create_food(
                self.state.width,
                self.state.height,
                [(self.state.width // 2, self.state.height // 2)],
            ),
        )

    def _detect_collision(self, position: Cell) -> bool:
        x, y = position
        if x < 0 or y < 0 or x >= self.state.width or y >= self.state.height:
            return True
        if position in self.state.snake:
            return True
        return False
