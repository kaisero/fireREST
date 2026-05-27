.PHONY: pre-commit mypy test docs docs-serve build check

pre-commit:
	uv run --group dev pre-commit run --all-files

mypy:
	uv run --group dev mypy fireREST

test:
	uv run --group dev pytest --cov=fireREST --cov-report=term

docs:
	DISABLE_MKDOCS_2_WARNING=true uv run --group docs mkdocs build --strict

docs-serve:
	DISABLE_MKDOCS_2_WARNING=true uv run --group docs mkdocs serve

build:
	uv build

check: pre-commit mypy test docs build
