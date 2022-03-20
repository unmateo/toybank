#!make
.DEFAULT_GOAL := help

help:
	make --help
install-dev:
	pip install -r requirements/dev.txt && pre-commit install
install-prd:
	pip install -r requirements/prd.txt
lint:
	python -m black . && python -m mypy toybank
run:
	uvicorn toybank.app:app
test:
	pytest tests/
