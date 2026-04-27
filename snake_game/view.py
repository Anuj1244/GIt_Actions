from __future__ import annotations

import tkinter as tk
from typing import Callable

from .model import GameModel, Direction

CELL_SIZE = 24
SNAKE_COLOR = "#2e7d32"
FOOD_COLOR = "#d32f2f"
BG_COLOR = "#fafafa"
GRID_COLOR = "#cfd8dc"


class GameView:
    def __init__(self, model: GameModel, on_direction_change: Callable[[Direction], None]) -> None:
        self.model = model
        self.on_direction_change = on_direction_change
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(
            self.root,
            width=model.state.width * CELL_SIZE,
            height=model.state.height * CELL_SIZE,
            bg=BG_COLOR,
        )
        self.canvas.pack()
        self.status = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.status.pack(pady=4)
        self._bind_keys()

    def _bind_keys(self) -> None:
        self.root.bind("<Up>", lambda event: self.on_direction_change(Direction.UP))
        self.root.bind("<Down>", lambda event: self.on_direction_change(Direction.DOWN))
        self.root.bind("<Left>", lambda event: self.on_direction_change(Direction.LEFT))
        self.root.bind("<Right>", lambda event: self.on_direction_change(Direction.RIGHT))

    def draw(self) -> None:
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_food()
        self._draw_snake()
        self.status.config(text=f"Score: {self.model.state.score}")
        if self.model.state.game_over:
            self.canvas.create_text(
                self.canvas.winfo_width() // 2,
                self.canvas.winfo_height() // 2,
                text="Game Over",
                fill="red",
                font=("Arial", 24, "bold"),
            )

    def _draw_grid(self) -> None:
        for x in range(self.model.state.width):
            x1 = x * CELL_SIZE
            self.canvas.create_line(x1, 0, x1, self.canvas.winfo_height(), fill=GRID_COLOR)
        for y in range(self.model.state.height):
            y1 = y * CELL_SIZE
            self.canvas.create_line(0, y1, self.canvas.winfo_width(), y1, fill=GRID_COLOR)

    def _draw_snake(self) -> None:
        for x, y in self.model.state.snake:
            self._draw_cell(x, y, SNAKE_COLOR)

    def _draw_food(self) -> None:
        x, y = self.model.state.food
        self._draw_cell(x, y, FOOD_COLOR)

    def _draw_cell(self, x: int, y: int, color: str) -> None:
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def run(self) -> None:
        self.root.mainloop()
