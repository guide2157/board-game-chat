# Board Game Chat API

A FastAPI application with health check endpoint and request/response logging middleware.

## Pre-requisites
1. [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager

## Setup

1. Create a virtual environment:
```bash
uv venv board-game-chat
```

2. Activate the virtual environment:
```bash
source board-game-chat/bin/activate
```

2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## Contributor Setup

Start the setup by installing dependencies by running
```bash
uv pip install -r requirements-dev.txt
```

### Pre-commit Hook Setup

We use [pre-commit](https://pre-commit.com/) to ensure code formatting and linting are automatically checked before any commit is made. This helps maintain code quality and consistency in the project.

To set up pre-commit in your environment, install the git hooks defined in `.pre-commit-config.yaml` by running
```bash
pre-commit install
```

This will make linting and formatting checks (using [ruff](https://docs.astral.sh/ruff/)) run automatically whenever you commit code.

To manually run the hooks on all files:
```bash
pre-commit run --all-files
```
