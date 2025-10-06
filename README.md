
uv init --lib calculator

cd calculator

mkdir -p tests

uv add pytest

uv run pytest tests

uv build