all: lint test

test:
	python -m unittest discover -s tests

lint:
	flake8
