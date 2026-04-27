"""Snake game package using MVC and Strategy patterns."""
from .controller import GameController
from .model import GameModel
from .view import GameView

__all__ = ["GameController", "GameModel", "GameView"]
