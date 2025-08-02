.PHONY: test format lint

test:
	@echo "Running tests..."
	pytest

format:
	@echo "Formatting code with Ruff..."
	ruff format src tests

lint:
	@echo "Checking lint with Ruff..."
	ruff check src tests

all: format lint test
