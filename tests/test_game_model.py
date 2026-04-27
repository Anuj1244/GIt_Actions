import pytest

from snake_game.model import GameModel, Direction


def test_initial_state():
    model = GameModel(width=10, height=8)
    assert len(model.state.snake) == 1
    assert model.state.score == 0
    assert model.state.food != model.state.snake[0]


def test_change_direction():
    model = GameModel(width=10, height=8)
    model.change_direction(Direction.DOWN)
    assert model.state.direction == Direction.DOWN
    model.change_direction(Direction.UP)
    assert model.state.direction == Direction.DOWN


def test_step_eats_food_and_scores():
    model = GameModel(width=5, height=5)
    model.state.snake = [(2, 2)]
    model.state.direction = Direction.RIGHT
    model.state.food = (3, 2)
    model.step()
    assert model.state.score == 1
    assert len(model.state.snake) == 2


def test_step_game_over_on_wall_collision():
    model = GameModel(width=3, height=3)
    model.state.snake = [(2, 1)]
    model.state.direction = Direction.RIGHT
    model.step()
    assert model.state.game_over is True


def test_step_game_over_on_self_collision():
    model = GameModel(width=5, height=5)
    model.state.snake = [(2, 2), (1, 2), (1, 3), (2, 3), (2, 2)]
    model.state.direction = Direction.LEFT
    model.step()
    assert model.state.game_over is True
