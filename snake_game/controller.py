from __future__ import annotations

from .model import GameModel, Direction
from .view import GameView


class GameController:
    def __init__(self, width: int = 20, height: int = 15) -> None:
        self.model = GameModel(width=width, height=height)
        self.view = GameView(self.model, self.change_direction)
        self.tick_time = 120

    def change_direction(self, direction: Direction) -> None:
        self.model.change_direction(direction)

    def start(self) -> None:
        self._schedule_tick()
        self.view.run()

    def _schedule_tick(self) -> None:
        if not self.model.state.game_over:
            self.model.step()
            self.view.draw()
            self.view.root.after(self.tick_time, self._schedule_tick)
        else:
            self.view.draw()
