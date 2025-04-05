# Vehicle Efficiency Label

# Development environment setup

1. Open the codebase with vscode.
1. A development container has been provided for development. Open the project in the development container.
    - Check [https://code.visualstudio.com/docs/devcontainers/containers](https://code.visualstudio.com/docs/devcontainers/containers) on how to open the project in the development container.
    - Otherwise, you can manually install the dependencies. Check [https://python-poetry.org/docs/](https://python-poetry.org/docs/) on how to install poetry and dependencies.
1. Run `poetry install` from the root project directory (where `pyproject.toml` is located) to install all the dependencies.
1. Run `poetry run exp` to run the `src/vehicle_efficiency_label/experiment.py` experiment script.
