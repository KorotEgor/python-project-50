package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

lint:
	poetry run flake8 difference_calculator

reinstall: build
	python3 -m pip install --user --force-reinstall dist/*.whl

test: lint
	poetry run pytest

env:
	python3 -m pip install poetry
	poetry install

