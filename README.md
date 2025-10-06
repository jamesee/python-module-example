
uv init --lib calculator

cd calculator

mkdir -p tests

uv add pytest

uv run pytest tests

uv build

uvx black tests

uvx ruff check tests
