# Board Game Chat API

A FastAPI application with health check endpoint and request/response logging middleware.

## Pre-requisites
1. [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager

## Setup

1. Create a virtual environment:
```bash
uv venv board-game-chat --python 3.12
```

2. Activate the virtual environment:
```bash
source board-game-chat/bin/activate
```

3. Navigate into the backend directory
```bash
cd backend
```

4. Put `PYTHONPATH` into your `.zshrc` or `.bash_profile`.
```bash
echo 'export PYTHONPATH="/path/to/backend:$PYTHONPATH"' >> ~/.zshrc
```
**You can get absolute path to the `backend` folder by running `pwd` command.**

**This only needs to be done once.**

5. Install dependencies:
```bash
uv pip install -r requirements.txt
```

6. Run the application:
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

### Unit tests
We use [pytest](https://pytest.org/) for running unit tests. All unit tests are located in the `backend/test` directory. To run the test suite and ensure your changes do not break any functionality, execute the following command from the `backend` directory:

```bash
pytest test
```

### Pre-commit Hook

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

### Mypy

Mypy is a static type checker for Python that helps catch type errors before runtime, enhancing code reliability. Our project is type-annotated, and we recommend running mypy to check for type issues during development. To perform a type check, run the following command from the `backend` directory:

```bash
mypy .
```
