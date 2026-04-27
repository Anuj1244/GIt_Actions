# Snake Game with GitHub Actions and Design Pattern

This repository contains a small snake game written in Python using a simple Model-View-Controller (MVC) structure and the Strategy pattern for direction control.

## Features

- MVC architecture (`snake_game.model`, `snake_game.view`, `snake_game.controller`)
- `Direction` strategy to prevent invalid reversal inputs
- `FoodFactory` to generate food in valid positions
- Unit tests for game logic
- GitHub Actions workflow for CI

## Run locally

1. Create a Python environment.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

Use the arrow keys to move the snake.

## GitHub Actions

The workflow defined in `.github/workflows/ci.yml` runs on every push and pull request. It installs dependencies and executes tests with `pytest`.

## Design patterns used

- MVC (Model-View-Controller)
- Strategy for direction validation
- Factory for food placement
